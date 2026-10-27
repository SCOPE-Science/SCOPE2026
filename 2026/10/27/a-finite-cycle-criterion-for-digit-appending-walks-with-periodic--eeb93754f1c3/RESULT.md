# A finite-cycle criterion for digit-appending walks with periodic-polynomial corrections

## Finding

Fix an integer \(b\ge2\), a positive integer \(P\), a positive rational \(A\), and polynomials \(Q_0,\ldots,Q_{P-1}\in\mathbb Q[X]\). Suppose that for every sufficiently large integer \(n\), the number
\[
a_n=A b^n+Q_{n\bmod P}(n)
\]
is a positive integer. An append step with index jump \(k\ge1\) and digit length \(t\ge1\) is the relation
\[
a_{n+k}=b^t a_n+d,\qquad d\in\mathbb Z,\quad0\le d<b^t.
\]
An infinite walk is a strictly increasing infinite sequence of indices connected by such steps. A walk has digit ceiling \(N\) if every step has \(t\le N\).

Call a residue \(r\in\{0,\ldots,P-1\}\) **good** when \(Q_r\) is the constant polynomial \(c_r\in[-1,0]\); write \(G\) for the set of good residues. For each integer \(N\ge1\), define a finite directed multigraph \(\mathcal G_N\) with vertex set \(G\): for every \(r\in G\) and \(k\in\{1,\ldots,N\}\), put the labelled edge \(r\xrightarrow{k}(r+k)\bmod P\) precisely when its destination \(s\) lies in \(G\) and
\[
d_{r,k}=c_s-b^kc_r\in\{0,\ldots,b^k-1\}.
\]

**Theorem.** Every append step starting sufficiently far along the sequence satisfies \(t=k\), including when digit lengths are unrestricted. For every \(N\ge1\), an infinite digit-ceiling-\(N\) walk exists **if and only if** \(\mathcal G_N\) contains a directed cycle. An infinite walk with no digit-length ceiling exists **if and only if** \(G\ne\varnothing\). In that case one already exists with digit ceiling \(P\). Consequently the least permissible ceiling is
\[
N_{\min}=\min_{C\text{ directed cycle in }\mathcal G_P}\ \max_{e\in C} k_e,
\]
with minimum of the empty family interpreted as \(+\infty\). Every sufficiently late part of every infinite walk visits only good residues and follows the corresponding labelled edges.

## Assumptions and scope

All quantifiers range over integer parameters as stated, and the positivity/integrality hypothesis is required only on a tail. Polynomial coefficients and \(A\) may be rational. The class is a natural subclass of integer-valued rational-coefficient recurrences: if \(D\) bounds the polynomial degrees, the shift operator \(E\) annihilates the tail by \((E-b)(E^P-1)^{D+1}\). The dominant characteristic root is the simple root \(b\); any other roots are roots of unity, possibly with polynomial factors. This theorem does not classify recurrences whose subdominant roots have modulus greater than one or whose dominant root is a distinct power of the base.

## Proof

**1. Uniform equality of index jump and digit length.** For \(n\) large, the correction terms satisfy \(|Q_r(x)|\le C(x+1)^D\) for all \(x\ge0\) and all residues. The exponential bound
\[
\sup_{k\ge1}\frac{(n+k+1)^D}{b^k}\le C_{b,D}(n+1)^D
\]
then gives, **uniformly** for every \(k\ge1\),
\[
\frac{a_{n+k}}{b^k a_n}=1+O\!\left(\frac{(n+1)^D}{b^n}\right).
\]
If an append step of length \(t\) exists, positivity yields
\[
1\le\frac{a_{n+k}}{b^t a_n}<1+\frac1{a_n}.
\]
Combining these formulas forces \(b^{k-t}\to1\) uniformly over all steps as \(n\to\infty\). Since distinct integral powers of the fixed integer \(b\) are separated from \(1\), there is a threshold, independent of \(k,t\), after which \(t=k\) for every step.

**2. Each infinite walk eventually stays on good residues.** Take an infinite walk whose starting index is beyond that threshold; call its successive indices \(n_0<n_1<\cdots\). Every step appends exactly the number of base-\(b\) digits equal to the index increment. Concatenating steps from \(n_i\) through \(n_j\) gives
\[
a_{n_j}=b^{n_j-n_i}a_{n_i}+D_{ij},\qquad0\le D_{ij}<b^{n_j-n_i}.
\]
Divide by the power of \(b\) and let \(j\to\infty\). Since the corrections grow at most polynomially, the left side tends to \(A b^{n_i}\). It follows that
\[
a_{n_i}\le A b^{n_i}\le a_{n_i}+1,
\qquad -1\le Q_{n_i\bmod P}(n_i)\le0.
\]
For a nonconstant rational polynomial, values along an unbounded integer progression eventually leave the bounded interval \([-1,0]\). A constant polynomial outside that interval never satisfies the inequality. Thus, every sufficiently late index in an infinite walk belongs to \(G\). For such a step, subtracting the geometric parts leaves exactly \(d=c_s-b^k c_r\), so the step is one of the graph edges when its digit length is at most \(N\).

**3. Finite cycles are necessary and sufficient.** A bounded-length infinite walk gives an infinite path in the finite graph \(\mathcal G_N\), which must contain a directed cycle. Conversely, choose a directed cycle and any sufficiently large index in the cycle's initial residue. Follow the listed index jumps, which are positive; each target residue agrees with its edge and each difference is the prescribed legal integer digit. Repetition of the cycle produces an infinite walk, because all indices remain in the integer positive tail.

**4. Unrestricted lengths and the sharp ceiling.** If \(G=\varnothing\), Step 2 rules out all infinite walks. If \(r\in G\), the jump \(k=P\) returns to the same residue and has digit
\[
d=(1-b^P)c_r.
\]
The bounds \(-1\le c_r\le0\) give \(0\le d\le b^P-1\); the integrality of \(a_{n+P}\) and \(a_n\) on the tail makes \(d\) an integer. Repeating this edge gives an infinite walk with ceiling \(P\). Therefore all finite minimal ceilings are at most \(P\); the bottleneck formula follows from the cycle criterion.

## Verification

The standalone `verify.py` uses exact rational arithmetic, constructs the finite graphs, computes their cycle thresholds, and compares 385 index/digit pairs in seven explicit families. It reports `CERTIFICATE_OK`. The general proof above is symbolic and does not infer an infinite-walk assertion from finitely many tests.

For a concrete sharp bottleneck, let \(b=2\), \(P=4\), \(A=1/3\), and let the periodic constants be
\[
(c_0,c_1,c_2,c_3)=(-1/3,-2/3,-1/3,1/3).
\]
All terms are eventually positive integers. The good residues are \(0,1,2\); the length-one graph has no cycle, while the jumps \(0\xrightarrow{1}1\xrightarrow{1}2\xrightarrow{2}0\) form a cycle, so \(N_{\min}=2\). For example, the index path \(4\to5\to6\to8\to9\to\cdots\) begins with terms \(5\to10\to21\to85\to170\to\cdots\), appending legal binary blocks of lengths \(1,1,2,1,\ldots\).

## Relationship to prior work

Mosahab, Boyyakar, Bruda, Kominers and Miller (2026), *On Digit-Appending Walks Along Linear Recurrences*, prove a bounded-digit necessary condition and an unrestricted-walk existence result when the dominant root and base are multiplicatively independent (Theorems 1.2–1.3). Their examples \(b^n-1\) and \(b^n+1\) show opposite behavior in the dependent case; the present theorem resolves existence and the exact minimal ceiling for the stated periodic-polynomial dependent-root family, not for all dependent recurrences. Kominers (2025) bounds walks along Fibonacci and selected Lucas recurrences whose dominant roots are not this integer base. Earlier concatenation results of Banks and Luca concern concatenating whole recurrence terms rather than freely chosen digit blocks. The exponential approximation ingredient is related to the 2026 paper's Lemma 2.2, but the infinite-path trapping argument and directed-cycle classification are additional.

## Limitations

The criterion requires an eventual polynomial-by-residue correction and positive integer terms. It does not determine every possible finite walk, nor arbitrary subdominant exponential recurrences. The published-literature comparison is not exhaustive and independent mathematical validation has not been performed. The test script is finite corroboration only.

## References

1. A. Mosahab, S. Boyyakar, G. Bruda, S. D. Kominers, S. J. Miller, *On Digit-Appending Walks Along Linear Recurrences*, arXiv:2610.18919v1, first public 2026-10-12, https://arxiv.org/html/2610.18919v1 .
2. S. D. Kominers, *Uniform Bounds for Digit-Appending Fibonacci Walks*, arXiv:2512.06446v1, first public 2025-12-06, https://arxiv.org/html/2512.06446v1 .
3. W. D. Banks and F. Luca, *Concatenations with Binary Recurrent Sequences*, Journal of Integer Sequences 8 (2005), https://cs.uwaterloo.ca/journals/JIS/VOL8/Banks/banks81.html .
