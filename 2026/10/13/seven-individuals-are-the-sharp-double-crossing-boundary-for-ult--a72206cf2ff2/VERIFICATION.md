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
The claim is a finite exact result about expected **rooted** phylogenetic diversity under sampling without replacement on a common, positive-edge ultrametric three-tip tree.

The embedded `verify_pd_double.py` carries out a logically exhaustive check for \(3\le N\le7\), without floating-point tolerances.

First, every strictly positive integer profile \((a,b,c)\) of census \(N\) is generated twice: directly with \(a\le b\) and independently by quotienting all ordered positive integer compositions under interchange of the sister counts. Both methods must return the same complete profile list, with counts \(1,2,4,6,9\).

Second, for each of the \(58\) unordered pairs, the expected PD difference at depth \(m\) is written as \(-H[u_m+(h/H)v_m]/\binom Nm\) using integer coefficients \(u_m,v_m\). Every affine root in the real interval \((0,1)\) is computed exactly. A rational sample in each open root cell and each interior root point is examined. In all, \(116\) exact parameter checks prove that the sign pattern never has two strict changes for \(N\le6\) and yields precisely the three reported open parameter windows at \(N=7\). This test **covers all real branch-length ratios**, not just a rational branch-length grid.

Third, the implementation of the edge-coverage formula is independently compared against a literal enumeration of each individual subsample and its subtree edge lengths at \(H=9,h=2\), for every profile and depth through \(N=7\). All \(130\) direct-subset checks pass.

Finally the witness difference sequence at depths \(2\) through \(6\) is checked as
\[
\left(\frac1{21},-\frac1{35},-\frac1{35},\frac17,\frac27\right).
\]
The same tree gives rooted PD \(9\) after one sampled individual and \(25\) at full census.

Run `python3 verify_pd_double.py`. The first output line is `VERIFY_OK`. The computation terminates deterministically and uses only Python standard library exact fractions and combinations.

The finite proof does not extend these claims beyond \(N=7\), to other sampling conventions, or to non-ultrametric trees. Independent audit has not been performed.
