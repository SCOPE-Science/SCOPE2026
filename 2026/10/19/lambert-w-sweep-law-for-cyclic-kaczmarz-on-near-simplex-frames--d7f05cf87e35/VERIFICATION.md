---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Under z=A_n^T y the error sweep is similar to (I−βL)^(-1)βU for β=α/(n−1). Its trailing principal block is strictly positive, and the other column is zero. The geometric vector (1,t,...,t^(n−1)) solves the eigenvector equations with eigenvalue t^n: the first equation gives t^(n−1)=βΣ_(j=0)^(n−2)t^j, and differences yield t^(n−1)(1+β−t)=β. The nonunit root in (0,1) is unique by the strictly increasing exponential average after t=exp(−x_n/n). Positivity identifies it as the Perron root and gives a real error trajectory attaining the spectral factor, not a claim about one-sweep norm. Row relabeling leaves the Gram matrix fixed. The exponential sums converge uniformly on compact intervals to I(x); rearrangement of I(x)=1/α yields W_(−1) since W_0 returns the extraneous x=0. The trapezoid formula gives S_n=I+(I−E)/(n−1)+O(n^(−2)), so inversion yields the stated positive correction since E>I and I'>0. At α↓0, log(1/α)=x−log x+o(1), giving r∞∼α/log(1/α). At α=1−ε, S_n'(0)=1/2 and S_n''(0)=(2n−1)/(6n), and x_n≤2ε/(1−ε) since S_n'(y)≥1/2 for y≥0. Third derivatives are uniformly bounded on this interval, so expansion and inversion give the stated dimension-uniform coefficient (4n−2)/(3n), including the limiting gap 2ε. Independently constructed small sweep matrices at (n,α)=(2,.4),(3,.5),(5,.8),(8,.95) matched the inferred spectral radius to about 10^(−12) or better; the independent n=2 check also gives α² exactly.

## originality

PASS

The underlying Gauss–Seidel representation, signed equicorrelation family, and characteristic-root method are established. The Sun–Ye root polynomial algebraically continues to the relevant negative sign; it does not itself designate the Perron root there or give the scaled dimension limit. The supported distinct result is the negative O(1/n) correlation spectral classification, including the selected real branch, the explicit finite-size correction and the dimension-uniform near-simplex law. Bounds on other sign regimes, fixed-sweep errors, or general norm characterizations do not supply this rate law.

## value

PASS

The near-simplex family is a natural symmetric approach to one-dimensional rank loss on which a cyclic projection rate can be resolved exactly. The sweep rate, including the dimension-uniform ratio of its gap to the Gram gap and the distinct small-coupling logarithmic law, is a substantive diagnostic unavailable from a generic norm estimate. The first correction also distinguishes the finite and limiting factors with a known sign. This is an exact invariant of this model, not a general algorithmic improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
