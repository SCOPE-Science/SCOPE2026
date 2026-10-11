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

The module is the canonical **left** Hilbert module \(\mathcal H=\mathcal A\) over a nonzero unital \(C^*\)-algebra, with \(\langle x,y\rangle=xy^*\). The system is \(\{I\}\), with wandering vector \(1\).

An element \(s\in\mathcal A\) generates a complete singleton Parseval frame exactly when
\[
xs^*sx^*=xx^*\quad(x\in\mathcal A),
\]
which is equivalent to \(s^*s=1\) by substituting \(x=1\). The reconstruction is exact: \(x=(xs^*)s\).

For any integer \(k\ge1\), the diagonal singleton frame condition reads
\[
\Big(\sum_i x_i s_i^*\Big)\Big(\sum_j s_j x_j^*\Big)
=\sum_i x_ix_i^*\quad(x\in\mathcal A^k).
\]
One-coordinate tests give \(s_i^*s_i=1\), and two-coordinate tests at complex coefficients \(1\) and \(\mathrm i\) give \(s_i^*s_j=0\) for different indices. The converse is immediate, with exact reconstruction \(x_j=(\sum_i x_i s_i^*)s_j\).

If \(v^*v=w^*w=1\) and \(v^*w=0\), the family \(s_j=v^{j-1}w\) consists of pairwise orthogonal isometries for every finite collection of indices. If such a pair does not exist, only \(k=1\) is admissible.

For an explicit instance, let \(\mathcal A=B(\ell^2(\mathbb N))\) and
\[
s_je_n=e_{2^{j-1}(2n-1)}.
\]
The images for distinct \(j\) are supported on disjoint power-of-two valuation classes, establishing \(s_i^*s_j=\delta_{ij}I\) for all positive integers \(i,j\). Hence the supremum of admissible \(k\) is infinite, while \(\{1\}\) remains a complete wandering vector.

For every positive integer \(k\), the nonzero positive elements \(\langle s_j,s_j\rangle=s_js_j^*\) have mutually orthogonal support and satisfy
\[
0\le\sum_{j=1}^k s_js_j^*\le1.
\]
This exactly satisfies the source proof's penultimate estimate and demonstrates why positivity supplies no contradiction.

The proof is uniform in \(k\); no finite computation is used as an infinite certificate. The source's Section 2 hypotheses, Section 5 multiplicity definition, Theorem 5.2 and Theorem 5.3 statement and proof were read in the original full text and inspected visually where needed. The earlier distinct multi-frame convention was checked against its original full-text Definition 2.6 and Sections 3--4.
