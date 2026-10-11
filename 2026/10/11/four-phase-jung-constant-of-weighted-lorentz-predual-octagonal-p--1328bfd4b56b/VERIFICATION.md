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

The proof's finite-dimensional primal linear program is
\[
\min_{c\in\mathbb R^2,R\in\mathbb R}R
\quad\text{subject to}\quad
R+f(c)\ge h_S(f)\qquad(f\in F).
\]
Its exact dual is
\[
\max\sum_f\alpha_fh_S(f),\qquad
\alpha_f\ge0,\quad\sum_f\alpha_f=1,\quad\sum_f\alpha_ff=0.
\]
The dual constraint matrix has rank three and the two circuit classes exhaust its extreme feasible points after isometric symmetries. Opposite-pair cases never exceed radius \(1/2\) for diameter one.

For the axis--axis--diagonal class, the three facet inequalities
\[
p_1+p_2\le k,\quad q_1+q_2\le k,\quad(p_1-q_1)-(p_2-q_2)\le k
\]
sum to \(2(p_1+q_2)\le3k\). The independent coordinate bound is \(p_1+q_2\le2\). Both are attained by the explicit Type I triples in RESULT.md.

For the axis--diagonal--diagonal class, the two inequalities
\[
p_1-p_2\le k,\qquad(p_1-q_1)+(p_2-q_2)\le k
\]
sum to \(2p_1-q_1-q_2\le2k\). The other upper bound \(3\) comes from three coordinate inequalities. All three Type II witness intervals in RESULT.md attain the smaller bound.

For reproducibility, the diameter-one status of each witness is checked solely by the four conditions \(|a|\le1\), \(|b|\le1\), \(|a+b|\le k\), and \(|a-b|\le k\) applied to each pairwise difference. An independent numerical radius linear program was evaluated at \(k=11/10,5/4,4/3,7/5,3/2,8/5,19/10\) and returned the predicted Jung constants \(33/31,15/13,6/5,20/17,6/5,15/13,30/29\) respectively. This finite check is ancillary, not an infinite proof.

No unproved extension is used. The regular-octagon special value was already independently known; the theorem's new content is the all-weight formula and its off-regular maxima. No independent review has been performed.
