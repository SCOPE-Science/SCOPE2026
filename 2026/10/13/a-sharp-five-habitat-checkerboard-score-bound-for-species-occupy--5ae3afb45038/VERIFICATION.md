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
The package includes an executable standard-library-only exact certificate.

Execute:

`python3 verify_checkerboard_five_sites.py`

Successful output ends with `VERIFY_OK`. The verifier uses exact integer determinants and rational Gaussian elimination to reconstruct every candidate from all nonempty supports of the ten habitat-pair types. It asserts a complete negative-tangent-Hessian candidate table and tests strict external gradient slack for every global winner. Therefore the finite certificate supplies a proof of the global real-simplex bound, not just a bounded-species numerical experiment.

The normalized objective is
\[
Q(x)=\sum_{e<f}w_{ef}x_ex_f,
\qquad
w_{ef}=\begin{cases}4,&e\cap f=\varnothing,\\1,&|e\cap f|=1.\end{cases}
\]
For five habitats, the stationary-face candidate table is \((\text{support size},Q,\text{count})\) equal to
\[
(1,0,10),\ (2,1/4,30),\ (2,1,15),\ (3,1/3,30),\ (3,16/15,30),\ (4,3/8,5),\ (4,12/11,10).
\]
No larger support has strictly negative tangent Hessian. At every winning point, positive-type gradient is \(24/11\) and zero-type gradient is \(17/11\).

Direct integer enumeration through eleven species checks 352,705 multiplicity vectors and obtains total-score maxima
\[
4,9,17,27,39,53,69,88,108,132
\]
for \(s=2,\ldots,11\). The eleven-species maximum has exactly ten occupancy multiplicity vectors and equals the theoretical continuous bound.

The script's second formula
\[
U=2s^2+\sum_e c_e^2-\frac32\sum_v d_v^2
\]
with \(d_v\) the number of species at habitat \(v\), independently crosschecks the original pairwise formula in all smaller enumeration cases.

No asymptotic, statistical, or infinite-census conclusion is inferred from the bounded brute-force check. The global claim instead follows from the exact finite support certificate and its analytic face-reduction argument. Independent audit is not performed.
