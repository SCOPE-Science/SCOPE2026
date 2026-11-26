'use strict';
const assert = require('node:assert/strict');
const words = n => Array.from({length:2**n}, (_,i)=>i.toString(2).padStart(n,'0'));
const flip = w => [...w].map(c=>c==='0'?'1':'0').join('');
const image = (v,x) => [...x].map(c=>c==='0'?v:flip(v)).join('');

// Does w contain a factor forbidden at the chosen 5/2 boundary?
function bad(w,weak) {
  for (let p=1;p<w.length;p++) {
    let r=0;
    for (let i=0;i+p<w.length;i++) {
      r=w[i]===w[i+p]?r+1:0;
      if (weak?2*(p+r)>5*p:2*(p+r)>=5*p) return true;
    }
  }
  return false;
}

const candidates=words(6).map(w=>'0'+w);
assert.equal(candidates.length,64);
assert.equal(bad('01',false),false);
assert.equal(bad('001',true),false);
assert.deepEqual(candidates.filter(v=>!bad(image(v,'01'),false)),[]);
const survivors=candidates.filter(v=>!bad(image(v,'001'),true));
assert.deepEqual(survivors,['0100110','0110010']);

const source=[1,2,3,4].flatMap(words).filter(w=>!bad(w,true));
assert.equal(source.length,22);
for (const v of survivors) {
  const f=flip(v);
  for (const x of [v,f]) {
    const p=Array.from({length:7},(_,i)=>i+1).find(j=>x.slice(j)===x.slice(0,7-j));
    assert.equal(p,6);
  }
  assert.ok(v[0]!==f[0] && v[6]!==f[6]);
  for (const x of [v,f]) for (const y of [v,f])
    for (let r=4;r<7;r++) assert.notEqual(x.slice(0,r),y.slice(7-r));
  for (const x of source) assert.equal(bad(image(v,x),true),false);
}
console.log('VERIFY_OK normalized=64 strict_failures=64 weak_failures=62 weak_survivors=0100110,0110010 admissible_inputs=22');
