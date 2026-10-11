---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The checked primary formulas are
\[
\det(zI-M_+)=(z-1)^{36}\left[z^2-(2-3m^2-m^3)z+1\right]
\]
and, after reversing the cyclic order, the same formula with \(m\) replaced by \(-m\). The source also gives
\[
m=1+\operatorname{tr}(S_*T_{[c]}).
\]

For \(a_+(m)=2-m^2(m+3)\), direct evaluation on \(m=-3,-2,-1,0,1\) gives \(2,-2,0,2,-2\). For \(m\ge2\), \(a_+(m)\le-18\). For \(m\le-4\), writing \(n=-m\ge4\) gives \(a_+(m)=2+n^2(n-3)\ge18\). Hence the unit-circle set for the plus orientation is exactly \(\{-3,-2,-1,0,1\}\), and sign reversal gives \(\{-1,0,1,2,3\}\) for the minus orientation.

For every reciprocal quadratic \(z^2-az+1\) with \(|a|>2\), the larger root modulus is
\[
\frac{|a|+\sqrt{a^2-4}}2.
\]
Thus \(|m|\ge4\) gives a lower bound at \(|a|=18\), namely \(9+4\sqrt5\), with equality for one orientation at each of \(m=4\) and \(m=-4\).

Running `python3 artifacts/verify_spectral_gap.py` returns:

`VERIFY_OK both_unit=-1,0,1 exactly_one=-3,-2,2,3 gap=9+4sqrt(5) equality=-4,4`

The finite loop is not the proof of the all-integer claim; the inequalities above are.

No independent audit has been performed.
