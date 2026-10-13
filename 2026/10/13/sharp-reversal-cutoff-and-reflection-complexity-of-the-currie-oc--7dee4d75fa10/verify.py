#!/usr/bin/env python3
H={"0":"01","1":"21","2":"0"}

def iterate(k):
    w="0"
    for _ in range(k):
        w="".join(H[c] for c in w)
    return w

def factors(w,n):
    return {w[i:i+n] for i in range(len(w)-n+1)}

def rclass_count(F):
    return len({min(u,u[::-1]) for u in F})

# The published factor-complexity theorem is rho(n)=2n+1.
# Once a finite prefix realizes that many factors, its factor set is exhaustive.
w=iterate(20)
expected_r={1:3,2:3,3:6,4:7,5:10,6:12,7:15,8:17}
reversible={}
for n in range(1,9):
    F=factors(w,n)
    assert len(F)==2*n+1, (n,len(F))
    assert rclass_count(F)==expected_r[n], (n,rclass_count(F))
    reversible[n]=sorted(u for u in F if u[::-1] in F)

assert reversible[7]==["1012101"]
assert reversible[8]==[]
assert set(reversible[6])=={"012101","101210"}

F8=sorted(factors(w,8))
expected8=[
"01021012","01210102","01210210","02101021","02101210",
"10102101","10121010","10121021","10210102","10210121",
"12101021","12102101","21010210","21012101","21012102",
"21021010","21021012"]
assert F8==expected8
assert all(u[::-1] not in set(F8) for u in F8)

# Independent longer-prefix regression: after the length-8 cutoff, every observed
# reflection class is a singleton and the published complexity count is met.
for n in range(8,41):
    F=factors(w,n)
    assert len(F)==2*n+1, (n,len(F))
    assert all(u[::-1] not in F for u in F), n
    assert rclass_count(F)==2*n+1

# Check primitivity of the defining substitution by reachability within three steps.
letters="012"
images={a:a for a in letters}
for _ in range(3):
    images={a:"".join(H[c] for c in images[a]) for a in letters}
assert all(set(images[a])==set(letters) for a in letters)

print("VERIFY_OK factor_sets_n=1..8_complete_by_rho=2n+1 "
      "reflection_profile=3,3,6,7,10,12,15,17 "
      "length7_only_reversible=1012101 length8_reversible=0 "
      "regression_n=8..40_no_reversals primitive_substitution=1")
