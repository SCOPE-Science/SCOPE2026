# Optimal two-window coverage and three-window burst covering for binary extended Hamming codes

## Finding

**Theorem.** Let \(m\ge2\), let \(q=2^m\), and let \(C\) be the length-\(q\) binary extended Hamming code. In any ordering \(\pi\) of its coordinates, let \(S_b^{\mathrm{lin}}(\pi)\) be the syndromes obtainable as sums of columns of a parity-check matrix supported inside some non-wrapping window of at most \(b\) consecutive positions. Let \(S_b^{\mathrm{cyc}}(\pi)\) be the analogous set when windows may wrap around the end. Then

\[
\max_\pi |S_2^{\mathrm{lin}}(\pi)|
=\max_\pi |S_2^{\mathrm{cyc}}(\pi)|=2q-1,
\]

while an explicit **single ordering** satisfies

\[
|S_2^{\mathrm{lin}}(\pi)|=|S_2^{\mathrm{cyc}}(\pi)|=2q-1,
\qquad
S_3^{\mathrm{lin}}(\pi)=S_3^{\mathrm{cyc}}(\pi)=\mathbb F_2^{m+1}.
\]

Thus the smallest possible burst-covering radius of the extended Hamming code, optimized over coordinate permutations, is exactly \(3\) in both the linear- and cyclic-window conventions, for every \(m\ge2\). At width two, **exactly one missing syndrome is unavoidable and sufficient**.

## Assumptions and scope

Represent the binary vector space of dimension \(m\) as \(F=\mathbb F_{2^m}\). Use the full-rank binary parity-check matrix \(H\) whose \(q\) columns, in an arbitrary order, are \(h(a)=(1,a)\in\mathbb F_2\oplus F\), one column for each \(a\in F\). Here the field is used only as an additive binary vector space in the parity checks. The kernel is the usual binary extended Hamming code with parameters \([q,q-m-1,4]_2\) (including the length-four member when \(m=2\)). The syndrome space has exactly \(2q\) elements.

A burst of span at most \(b\) means a binary error vector whose support is included in a consecutive window of length \(b\), irrespective of the number of nonzero error positions in the window. Cyclic windows use indices modulo \(q\); linear windows do not wrap. The result optimizes coordinate orderings of this fixed code, **not** all codes with the same parameters, and makes no claim about burst-error correction.

## Proof

**1. Two-window syndromes.** For an arbitrary ordering \((a_0,\ldots,a_{q-1})\) of \(F\), the empty error yields \((0,0)\), and single-coordinate errors yield all \(q\) odd-parity syndromes \((1,a)\). Every nonzero even-parity syndrome produced inside a two-window has the form \((0,a_i+a_{i+1})\), including \(i=q-1\) and the cyclic successor \(a_0\) in the cyclic case. Conversely every listed adjacent sum is realizable. If \(D(\pi)\) is the set of distinct nonzero adjacent differences in the convention concerned, then

\[
|S_2(\pi)|=q+1+|D(\pi)|.
\]

These differences cannot include all \(q-1\) nonzero field elements. Indeed, their sum over \(F\setminus\{0\}\) is zero for \(m\ge2\). For non-wrapping windows, having all \(q-1\) distinct differences would imply

\[
0=\sum_{i=0}^{q-2}(a_i+a_{i+1})=a_0+a_{q-1}\ne0,
\]

contradiction. For cyclic windows there are \(q\) adjacent differences, all nonzero. If all \(q-1\) nonzero elements occurred, exactly one nonzero difference would occur twice; their XOR would therefore be that nonzero difference. But the cyclic telescoping XOR is zero. Therefore \(|D(\pi)|\le q-2\) and in either convention \(|S_2(\pi)|\le2q-1\). In particular, no ordering has burst-covering radius two or less.

**2. Sharp ordering.** Choose any multiplicative generator \(\alpha\) of \(F^\times\), and order the column labels as

\[
(0,1,\alpha,\alpha^2,\ldots,\alpha^{q-2}).
\]

Write \(\alpha+1=\alpha^t\). Since \(\alpha\) is primitive and \(\alpha+1\) is neither \(1\) nor \(\alpha\), one has \(2\le t\le q-2\). The \(q-2\) differences internal to the consecutive powers are

\[
\alpha^j+\alpha^{j+1}=(1+\alpha)\alpha^j
\quad(0\le j\le q-3),
\]

and are pairwise distinct. The only nonzero difference absent from this list is

\[
\Delta=(1+\alpha)\alpha^{q-2}=\alpha^{t-1}.
\]

The initial difference \(0+1=1\), and the cyclic closing difference \(\alpha^{q-2}+0=\alpha^{q-2}\), both already belong to the internal list: their multiplicative exponents, \(0\) and \(q-2\), are distinct from the missing exponent \(t-1\in[1,q-3]\). Hence both conventions have precisely \(q-2\) distinct adjacent differences and consequently **exactly** \(2q-1\) two-window syndromes. Their unique missing syndrome is \((0,\Delta)\).

**3. The missing syndrome appears in a three-window.** Set \(j=q-2-t\); the range for \(t\) gives \(0\le j\le q-4\). Thus \(\alpha^j\) and \(\alpha^{j+2}\) occur at positions of the ordering separated by exactly two. Their sum is

\[
\alpha^j+\alpha^{j+2}
=(1+\alpha^2)\alpha^j
=(1+\alpha)^2\alpha^j
=\alpha^{2t+j}
=\alpha^{t-1}=\Delta,
\]

where the penultimate equality is modulo the multiplicative period \(q-1\). These two positions lie in one ordinary three-window, giving syndrome \((0,\Delta)\). Every other syndrome was already present in a two-window. Therefore all \(2q\) syndromes occur within ordinary three-windows, hence also cyclic three-windows. The impossibility at width two proves both optimal radii are exactly three. \(\square\)

## Verification

The included standalone Python 3 script `verify.py` uses no third-party packages. Run `python3 verify.py`. For the primitive binary-field models of degrees \(2\) through \(8\), it independently enumerates all error syndromes arising in ordinary and cyclic windows of widths two and three, checks that precisely one syndrome is absent at width two and none at width three, and verifies the set of adjacent/two-step differences. It also exhausts all \(6\) and \(5040\) translation-normalized orderings for \(m=2\) and \(m=3\), respectively, checking two-window impossibility in both conventions. Expected final output: `VERIFY_OK`.

These finite tests are **not** an exhaustive argument for unbounded \(m\). The all-rank conclusion follows from the telescoping obstruction and finite-field identities proved above; the finite checks are independent consistency tests.

## Relationship to prior work

Sac Himelfarb and Schwartz introduced the burst-covering setting, proved the syndrome-window characterization (their Theorem 13), and gave an example of an ordering of the length-eight extended Hamming code with burst-covering radius three (Example 16). That example establishes the case \(m=3\), not the all-\(m\) optimality or the sharp one-missing-syndrome statement. Their general counting bounds (Theorem 17) do not yield the present parity obstruction or the primitive-power construction.

The combinatorial obstruction has a natural relation to terraces and group sequencings: a complete list of distinct nonzero consecutive differences would be impossible in an elementary abelian binary group. That neighboring theory is not claimed as new, and the existence of some possible historical rephrasing is noted below. The new coding-theoretic statement pairs the sharp deficiency at width two with an explicit all-length, width-three optimal ordering and an exact syndrome certificate.

## Limitations

The theorem assumes binary extended Hamming codes and optimizes only coordinate permutations; it does not assert a bound for arbitrary linear codes or generic nonbinary extensions. No classification of **all** extremizing permutations is claimed. The proof does not show that a three-window representation is unique or that three-burst decoding is possible. An older result formulated through near-terraces or binary group orderings could potentially imply part or all of this theorem; that residual historical overlap is not ruled out merely by a database search.

## References

1. G. Sac Himelfarb and M. Schwartz, *On the Burst-Covering Radius of Binary Cyclic Codes*, arXiv:2601.00435 (first posted January 1, 2026), especially Theorem 13, Example 16, Theorem 17, and conclusion. https://arxiv.org/abs/2601.00435 .
2. M. A. Ollis and D. T. Willmott, *Constructions for Terraces and R-Sequencings, Including a Proof That Bailey's Conjecture Holds for Abelian Groups*, Journal of Combinatorial Designs 23 (2015), 1–17; first online 2014. DOI:10.1002/jcd.21396. Cited as related group-ordering background; only accessible abstract and metadata were compared, not a complete proof.
