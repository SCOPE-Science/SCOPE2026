'use strict';
// Exhaustive small-graph computation for the minimum decycling sets of GP(n,2).
function graph(n) {
  const V=2*n, adj=Array(V).fill(0), edges=[];
  function edge(a,b){if(a>b)[a,b]=[b,a];if((adj[a]&(1<<b))===0){adj[a]|=1<<b;adj[b]|=1<<a;edges.push([a,b]);}}
  for(let i=0;i<n;i++){edge(i,(i+1)%n);edge(i,n+i);edge(n+i,n+(i+2)%n);}
  return {n,V,adj,edges};
}
function forest(G, keep) {
 const parent=Array.from({length:G.V},(_,i)=>i);
 function find(i){while(parent[i]!==i){i=parent[i];}return i;}
 for(const [a,b] of G.edges)if((keep&(1<<a))&&(keep&(1<<b))){let x=find(a),y=find(b);if(x===y)return false;parent[x]=y;}
 return true;
}
function pop(x){let n=0;while(x){n++;x&=x-1;}return n;}
function inspect(n) {
 const G=graph(n), full=(1<<G.V)-1;
 let k=0,sets=[];
 for(;k<G.V;k++){sets=[];for(let mask=0;mask<=full;mask++)if(pop(mask)===k&&forest(G,full^mask))sets.push(mask);if(sets.length)break;}
 const ix=new Map(sets.map((x,i)=>[x,i]));
 const TJ=sets.map(()=>[]),TS=sets.map(()=>[]);
 for(let i=0;i<sets.length;i++)for(let j=i+1;j<sets.length;j++){
  const a=sets[i]&~sets[j],b=sets[j]&~sets[i];if(pop(a)===1&&pop(b)===1){TJ[i].push(j);TJ[j].push(i);const u=31-Math.clz32(a),v=31-Math.clz32(b);if(G.adj[u]&(1<<v)){TS[i].push(j);TS[j].push(i);}}
 }
 function components(A) {
  const seen=new Set(),comps=[];
  for(let i=0;i<A.length;i++)if(!seen.has(i)){const q=[i];seen.add(i);
   for(let qi=0;qi<q.length;qi++)for(const j of A[q[qi]])if(!seen.has(j)){seen.add(j);q.push(j);}comps.push(q);}
  return comps;
 }
 function breadth(A,s){let d=Array(A.length).fill(-1),q=[s];d[s]=0;for(let i=0;i<q.length;i++)for(const u of A[q[i]])if(d[u]<0){d[u]=d[q[i]]+1;q.push(u);}return d;}
 const cc=components(TS);let tjdiam=null,tjr=null,ecc=[];
 if(sets.length<=1000){ecc=TJ.map((_,i)=>Math.max(...breadth(TJ,i)));tjdiam=Math.max(...ecc);tjr=Math.min(...ecc);}
 const hist=A=>Object.fromEntries([...new Set(A)].sort((a,b)=>a-b).map(x=>[x,A.filter(z=>z===x).length]));
 return {n,k,sets, G,TJ,TS,components:cc.map(x=>x.length).sort((a,b)=>a-b),tc:components(TJ).map(x=>x.length).sort((a,b)=>a-b),td:hist(TJ.map(a=>a.length)),tsd:hist(TS.map(a=>a.length)),tse:TS.reduce((a,b)=>a+b.length,0)/2,te:TJ.reduce((a,b)=>a+b.length,0)/2, tjdiam,tjr,eccHist:hist(ecc)};
}
const expect={5:{k:3,N:20,ts:[...Array(20)].map(()=>1),tc:[4,4,4,4,4]},6:{k:4,N:120,ts:[120],tc:[120]},7:{k:4,N:70,ts:[...Array(14)].map(()=>1).concat(Array(14).fill(2),Array(7).fill(4)),tc:[70]}};
for(const n of [5,6,7]){
 const o=inspect(n),e=expect[n];
 function ok(b,s){if(!b)throw Error(n+': '+s);}
 ok(o.k===e.k&&o.sets.length===e.N,'optimum');
 ok(JSON.stringify(o.components)===JSON.stringify(e.ts),'slide components');
 ok(JSON.stringify(o.tc)===JSON.stringify(e.tc),'jump components');
 if(n===7){ok(o.tse===35 && o.te===140 && o.tjdiam===7 && o.tjr===6,'GP7 metrics');
  ok(JSON.stringify(o.tsd)==='{"0":14,"1":42,"2":14}','GP7 degrees');
  const components=[];const seen=new Set();for(let i=0;i<o.sets.length;i++)if(!seen.has(i)){
   const q=[i];seen.add(i);for(let j=0;j<q.length;j++)for(const v of o.TS[q[j]])if(!seen.has(v)){seen.add(v);q.push(v);}
   const h=q.map(v=>o.TS[v].length).sort((a,b)=>a-b).join(',');
   ok((q.length===1&&h==='0')||(q.length===2&&h==='1,1')||(q.length===4&&h==='1,1,2,2'),'component is paths');
  }
  // Every smallest decycling set is independent; its complement is an induced tree.
  for(const mask of o.sets){for(const [a,b] of o.G.edges)ok(!((mask&(1<<a))&&(mask&(1<<b))),'independence');}
  const rots=s=>{let t=0;for(let v=0;v<o.G.V;v++)if(s&(1<<v)){const w=v<n?(v+1)%n:n+(v-n+1)%n;t|=1<<w;}return t;};
  const refl=s=>{let t=0;for(let v=0;v<o.G.V;v++)if(s&(1<<v)){const w=v<n?(n-v)%n:n+(n-(v-n))%n;t|=1<<w;}return t;};
  const all=new Set(o.sets),visited=new Set(),rep=[];
  for(const s of o.sets)if(!visited.has(s)){const orbit=new Set();let z=s;for(let j=0;j<n;j++){orbit.add(z);orbit.add(refl(z));z=rots(z);}for(const t of orbit){ok(all.has(t),'orbit valid');visited.add(t);}rep.push({representative:[...Array(o.G.V).keys()].filter(x=>s&(1<<x)),size:orbit.size});}
  ok(rep.length===5&&rep.every(x=>x.size===14),'five dihedral orbits');
  console.log('GP7_orbits',JSON.stringify(rep));
 }
 console.log(JSON.stringify({n,optimum:o.k,states:o.sets.length,slide_components:o.components.reduce((d,x)=>(d[x]=(d[x]||0)+1,d),{}),jump_components:o.tc,tj_edges:o.te,ts_edges:o.tse,slide_degrees:o.tsd,jump_degrees:o.td,jump_diameter:o.tjdiam,jump_radius:o.tjr,jump_eccentricities:o.eccHist}));
}
console.log('DIRECT_CHECK_PASS');
