---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Stationarity of X−x=Y gives Ey=0. Stationarity of X²−x² gives E[xY]=−E[y²]/2. Stationarity of XY−xy gives E[xy]=E[xY]+E[y²]=E[y²]/2; hence Cov(x,y)=Var(y)/2. Taking expectations in Y=(1+eps)y+kx(x−1)+mu xy gives k E[x(x−1)]+mu Var(y)/2=0. When k>0,mu<0, Var(y)=0 forces y=Y=0 and x∈{0,1} a.s.; otherwise E[(x−1/2)²]=1/4−mu Var(y)/(2k)>1/4, so a positive fraction of mass lies outside x∈[0,1]. Covariance PSD yields Vx>=Vy/4. At nonzero-variance equality, x−E x=y/2 a.s.; invariance of same relation at image and X=x+Y force Y=−y, X−E x=−(x−E x), so T²=id a.s. This is exact symbolic stationarity and Cauchy rigidity, not an inference from numerical orbits; an actual two-cycle in the sign regime k=2,mu=−1,eps=−1 realizes the reflection equality.

## originality

PASS

Best-of-knowledge: the classical Bogdanov-map papers study local bifurcation and chaos, while a fully inspected separately published period-two classification studies points not the universal invariant-measure covariance or global measure-strip inequality. The analogous Rulkov shear law concerns another map and does not imply Bogdanov specific k,mu strip identity. The original Bogdanov article was inaccessible in full in this run, so exact historic priority remains a stated material risk; lack of access alone is not a FAIL.

## value

PASS

PASS: For a canonical nonlinear map with a supercritical-Hopf regime, the exact all-stationary-states second-moment constraint yields a nonlocal forbidden-support strip and sharp 2-cycle equality rigidity. These are mathematically motivated restrictions on periodic and chaotic invariant states, rather than an arbitrary covariance sample; they do not assert existence of a chaotic measure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
