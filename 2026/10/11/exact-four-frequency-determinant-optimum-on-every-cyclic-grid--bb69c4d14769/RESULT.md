# Exact four-frequency determinant optimum on every cyclic grid

## Finding
For every integer \(N\ge4\), let \(G=\mathbb Z_N\), \(E=\{0,1,2,3\}\subset G\), and \(\omega_N=e^{2\pi i/N}\). For every unordered four-element subset \(B\subset G\), let \(T(E,B)\) be the unnormalized Fourier restriction matrix with entries \(\omega_N^{jk}\) for \(j\in E\) and \(k\in B\). Define its maximum determinant
\[
D_N=\max_{B\subset G,\ |B|=4}|\det T(E,B)|.
\]
Write \(N=4q+r\) with integers \(q\ge1\) and \(r\in\{0,1,2,3\}\). Then the exact maximum is
\[
D_N=\begin{cases}
16,&r=0,\\
64\sin^3(\pi q/N)\sin(\pi(q+1)/N)\cos^2(\pi/(2N)),&r=1,\\
16\cos^2(\pi/N),&r=2,\\
64\sin(\pi q/N)\sin^3(\pi(q+1)/N)\cos^2(\pi/(2N)),&r=3.
\end{cases}
\]
All maximizing frequency sets can be described exactly. List the four distinct residues in increasing order as \(b_1<b_2<b_3<b_4\), and put
\[
(a,b,c,d)=(b_2-b_1,b_3-b_2,b_4-b_3,N+b_1-b_4).
\]
These are the four positive *cyclic gaps*. The set \(B\) attains \(D_N\) **if and only if** its cyclic gap tuple is, up to cyclic rotation,
\[
\begin{array}{ll}
(q,q,q,q),&r=0,\\
(q,q,q,q+1),&r=1,\\
(q,q+1,q,q+1),&r=2,\\
(q,q+1,q+1,q+1),&r=3.
\end{array}
\]
The number of maximizing *literal four-element subsets* is exactly
\[
\#\{B:|B|=4,\ |\det T(E,B)|=D_N\}=\frac{N}{\gcd(N,4)}.
\]
In particular, when \(N\equiv2\pmod4\), making the four gaps as close to equal as possible is **not enough**: the two larger gaps must be separated by smaller gaps rather than adjacent.

## Assumptions and scope
Frequencies are distinct residues in \(\mathbb Z_N\); they are not ordered or counted with multiplicity. The character convention is \(\omega_N^{jk}\), with no matrix normalization. The same absolute determinant results for the conjugate convention. The Fourier matrix uses four consecutive sample points; no claim concerns an arbitrary four-point sample set. The determinant measures volume of this particular exponential basis, not its exact optimal condition number or the determinant of arbitrary matrices of roots of unity.

## Proof
**Step 1: a six-chord identity.** Put \(z_s=\omega_N^{b_s}\) for \(1\le s\le4\). Since consecutive Fourier rows have exponents \(0,1,2,3\), the determinant is the Vandermonde product \(\prod_{s<t}(z_t-z_s)\). The chord identity \(|e^{2\pi iu/N}-e^{2\pi iv/N}|=2\sin(\pi|u-v|/N)\), together with \(\sin(\pi u/N)=\sin(\pi(N-u)/N)\), yields
\[
|\det T(E,B)|=64\sin\frac{\pi a}{N}\sin\frac{\pi b}{N}\sin\frac{\pi c}{N}\sin\frac{\pi d}{N}\sin\frac{\pi(a+b)}{N}\sin\frac{\pi(b+c)}{N}.
\]
Here \(a,b,c,d\) are positive integers adding to \(N\), so every sine factor is positive. Conversely every such integer gap quadruple produces a four-set, up to translation.

**Step 2: opposite gaps differ by at most one.** Let \(f(t)=\log\sin(\pi t/N)\) for \(0<t<N\). Direct differentiation gives
\[
f''(t)=-\frac{\pi^2}{N^2}\csc^2\frac{\pi t}{N}<0,
\qquad f(N-t)=f(t).
\]
The log determinant, less the constant \(\log64\), is
\[
L(a,b,c,d)=f(a)+f(b)+f(c)+f(d)+f(a+b)+f(b+c).
\]
Fix \(b,d\) and the sum \(a+c\). The variable part of \(L\) is \(f(a)+f(c)+f(b+a)+f(b+c)\), strictly concave in \(a\) and invariant under \(a\leftrightarrow c\). Its integer maximum occurs exactly when \(|a-c|\le1\). Likewise, fixing \(a,c\) and \(b+d\), the variable part \(f(b)+f(d)+f(a+b)+f(b+c)\) is strictly concave in \(b\) and invariant under \(b\leftrightarrow d\); the latter invariance uses \(a+b+c+d=N\) and \(f(N-t)=f(t)\). Thus every global maximizing quadruple obeys
\[
|a-c|\le1,\qquad |b-d|\le1.
\]

**Step 3: opposite-pair totals differ by at most two.** Write \(A=a+c\) and \(B_0=b+d=N-A\). Suppose \(A-B_0\ge3\). The pairwise balancing just obtained forces \(a,c\ge b,d+1\) (each of the two left gaps is strictly greater than each right gap). Replace
\[
(a,b,c,d)\longmapsto(a-1,b+1,c-1,d+1).
\]
All transformed gaps remain positive and still sum to \(N\); the two diagonal arguments \(a+b\) and \(b+c\) are unchanged. Strict concavity of \(f\) shows that each of the transfers from the larger gaps \(a,c\) to the smaller gaps \(b,d\) weakly raises the sum of their four \(f\)-values, and at least one transfer strictly raises it because \((a-b)+(c-d)=A-B_0\ge3\). This contradicts maximality. The opposite case \(B_0-A\ge3\) is symmetric. Hence
\[
|A-B_0|\le2.
\]
Together with Step 2, this leaves only the following exhaustive integer configurations.

**Step 4: classify the four residue cases.** If \(N=4q\), the tuple \((q,q,q,q)\) makes all four characters pairwise orthogonal, so Hadamard's inequality gives the global bound \(16\), attained there. Equality in Hadamard forces column orthogonality. Equivalently the Vandermonde nodes must form a rotated set of four fourth roots of unity, whose cyclic gaps are all \(q\); thus there are no other optimizers.

If \(N=4q+1\) or \(N=4q+3\), the opposite-pair totals have odd sum. By Step 3 their difference must be \(1\), so Steps 2–3 force respectively three gaps \(q\) and one \(q+1\), or one gap \(q\) and three \(q+1\). Every cyclic rotation yields the same determinant, and the six-chord identity gives the respective formulas in the theorem (both diagonal sines equal \(\cos(\pi/(2N))\)).

If \(N=4q+2\), the possible opposite-pair total differences are \(0\) and \(2\). Difference \(0\) forces \(a,c\) to be \(q,q+1\) in some order and \(b,d\) likewise; the resulting *adjacent-large-gaps* pattern has diagonal sine product \(\cos(\pi/N)\). Difference \(2\) forces \(a=c=q\), \(b=d=q+1\), or vice versa; this *alternating* pattern has both diagonal sines equal to \(1\). Both patterns have the same four single-gap sine factors. Since \(\cos(\pi/N)<1\), only the alternating configuration maximizes, with determinant \(16\cos^2(\pi/N)\).

**Step 5: count the maximizing subsets.** Translation by one permutes the sets for each permitted cyclic gap pattern. In the odd residue classes the unique gap of different size distinguishes a starting point, so the translation orbit has size \(N\). For \(N\equiv2\pmod4\), an alternating pattern has exactly the translation symmetry by \(N/2\), so the orbit size is \(N/2\). For \(4\mid N\), the set is a translate of the order-four subgroup and has fourfold translation stabilizer, so there are \(N/4\) translates. These cases give \(N/\gcd(N,4)\) exactly. All converses are attained by constructing the indicated positive gaps.

## Verification
The standalone `verify.py` uses the Python standard library, computes each \(4\times4\) determinant independently through its \(24\)-permutation Leibniz expansion, and compares it to the six-chord identity. It exhausts all \(\binom N4\) frequency subsets for every \(4\le N\le24\) (\(53{,}130\) total), confirms the theorem's maximum and every maximizing subset, and confirms the count \(N/\gcd(N,4)\). Running `python3 verify.py` gives the final line `CHECK_OK 53130`.

These numerical tests are corroboration only. The five analytic steps above establish the formulas, complete optimizer classification and count for **every** integer \(N\ge4\), without extrapolating from finite data.

## Relationship to prior work
Ferguson–Mayeli–Sothanaphan, arXiv:1904.04487, Definitions 3.9–3.10, define exactly the determinant invariant \(D(E)=\max_{|B|=|E|}|\det T(E,B)|\) for finite-group exponential bases and motivate its significance as a quantitative spectrality measure. Their general discussion gives existence and upper bounds but does not determine this fixed four-consecutive-point cyclic family or classify its determinant-maximizing frequency sets.

Dubickas–Pritsker, arXiv:1902.08348, Section 1, recall that unconstrained four-node Fekete points on the **continuous** unit circle are the vertices of a square. This supplies the continuous bound \(16\), not the exact loss caused by restricting nodes to the \(N\)-th roots of unity, and it does not imply the residue-dependent optimizer census.

Results on discrete Kronecker approximation, finite cyclic spectral four-sets, and determinants for a different subgroup-plus-point family concern different objective functions or different Fourier matrix rows. Direct statement-and-implication comparisons found no covering result for the four-consecutive-row volume optimum.

## Limitations
The theorem is exact for four consecutive rows only and for the **unnormalized** determinant. It does not supply the best singular-value ratio, arbitrary-node-count discrete Fekete configurations, or arbitrary sampled row sets. Numerical checks use floating-point arithmetic and are not an independent mathematical certificate. An equivalent older discrete-Fekete or optimal-design theorem under different terminology may have escaped the literature search; neither unpublished uniqueness nor independent validation is claimed.

## References
1. A. Dubickas and I. E. Pritsker, *Weighted Fekete points on the real line and the unit circle*, arXiv:1902.08348v1, first public posting 2019-02-22, https://arxiv.org/abs/1902.08348.
2. S. Ferguson, A. Mayeli, and N. Sothanaphan, *Riesz bases of exponentials and multi-tiling in finite abelian groups*, arXiv:1904.04487v1, first public posting 2019-04-09, https://arxiv.org/abs/1904.04487.
