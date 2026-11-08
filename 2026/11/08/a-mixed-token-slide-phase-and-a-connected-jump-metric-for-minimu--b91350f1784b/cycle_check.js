'use strict';
// Independent cycle-hitting verifier: no forest test, parent DSU, or search code shared.
function adjacency(n){let a=Array.from({length:2*n},()=>[]);function add(i,j){if(!a[i].includes(j)){a[i].push(j);a[j].push(i);}}
 for(let j=0;j<n;j++){add(j,(j+1)%n);add(j,n+j);add(n+j,n+(j+2)%n);}return a;}
function cycles(n,A){let seen=new Set();const c=[];let N=2*n;
 for(let root=0;root<N;root++){
  function visit(path,mask){let v=path[path.length-1];for(const w of A[v]){
    if(w===root&&path.length>=3){if(path[1]<v){const z=path.reduce((m,u)=>m|(1<<u),0);if(!seen.has(z)){seen.add(z);c.push(z);}}}
    else if(w>root && !(mask&(1<<w)))visit([...path,w],mask|(1<<w));
  }}
  visit([root],1<<root);
 }
 return c;
}
function ones(n,k){let out=[];function rec(v,remaining,mask){if(remaining===0){out.push(mask);return;}if(v>=n||n-v<remaining)return;rec(v+1,remaining-1,mask|(1<<v));rec(v+1,remaining,mask);}rec(0,k,0);return out;}
function countbits(x){let z=0;while(x){z++;x&=x-1;}return z;}
function get(n,k){const A=adjacency(n),C=cycles(n,A), S=ones(2*n,k).filter(m=>C.every(c=>(m&c)!==0));
 let full=new Set(S);const slide=new Map(S.map(x=>[x,new Set()])),jump=new Map(S.map(x=>[x,new Set()]));
 for(const s of S)for(let u=0;u<2*n;u++)if((s>>u)&1)for(let v=0;v<2*n;v++)if(!((s>>v)&1)){
  let t=(s^(1<<u))|(1<<v);if(!full.has(t))continue;
  jump.get(s).add(t);if(A[u].includes(v))slide.get(s).add(t);
 }
 function cc(G){let seen=new Set(),sizes=[];for(const s of S)if(!seen.has(s)){let q=[s];seen.add(s);for(let i=0;i<q.length;i++)for(const v of G.get(q[i]))if(!seen.has(v)){seen.add(v);q.push(v);}sizes.push(q.length);}return sizes.sort((a,b)=>a-b);}
 function ecc(G,s){let d=new Map([[s,0]]),q=[s];for(let i=0;i<q.length;i++)for(const v of G.get(q[i]))if(!d.has(v)){d.set(v,d.get(q[i])+1);q.push(v);}return Math.max(...d.values());}
 return {n,k,cycles:C.length,states:S.length,slide_components:cc(slide),jump_components:cc(jump),slide_edges:[...slide.values()].reduce((z,s)=>z+s.size,0)/2,jump_edges:[...jump.values()].reduce((z,s)=>z+s.size,0)/2,ts_degree:[...slide.values()].map(x=>x.size).sort((a,b)=>a-b),tj_ecc:S.map(s=>ecc(jump,s)).sort((a,b)=>a-b)};
}
let d=[];
for(const [n,k] of [[5,3],[6,4],[7,4]]){
 const r=get(n,k);d.push(r);
 const expect=n===5?[20,0,30,20]:n===6?[120,354,666,1]:[70,35,140,35];
 if(r.states!==expect[0]||r.slide_edges!==expect[1]||r.jump_edges!==expect[2]||r.slide_components.length!==expect[3])throw Error('cycle mismatched '+n);
 if(n===7){let hist={};for(const s of r.slide_components)hist[s]=(hist[s]||0)+1;
 if(JSON.stringify(hist)!==JSON.stringify({'1':14,'2':14,'4':7}))throw Error('components');
 if(r.tj_ecc[0]!==6||r.tj_ecc.at(-1)!==7||r.tj_ecc.filter(x=>x===7).length!==14)throw Error('metric');}
 console.log(JSON.stringify({n:r.n,cycles_checked:r.cycles,states:r.states,slide_edges:r.slide_edges,jump_edges:r.jump_edges,slide_components:r.slide_components.length,jump_components:r.jump_components,diameter:r.tj_ecc.at(-1),radius:r.tj_ecc[0]}));
}
console.log('CYCLE_CHECK_PASS');
