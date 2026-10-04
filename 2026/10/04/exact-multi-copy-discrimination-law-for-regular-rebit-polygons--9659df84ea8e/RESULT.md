# Exact multi-copy discrimination law for regular rebit polygons
## Finding
For integers \(N\ge 3\) and \(k\ge 1\), consider the regular real-qubit projective ensemble
\[
|\psi_a\rangle=\cos(\pi a/N)|0\rangle+\sin(\pi a/N)|1\rangle,
\qquad a=0,\ldots,N-1,
\]
with equal prior \(1/N\), observed through \(k\) identical copies. Put
\[
p_r^{(N,k)}=2^{-k}\!\sum_{\substack{0\le j\le k\\ j\equiv r\pmod N}}\binom{k}{j},
\qquad r=0,\ldots,N-1.
\]
Then the spectrum of the weighted Gram matrix, with zeros retained when a residue class is empty, is exactly
\[
\{p_0^{(N,k)},\ldots,p_{N-1}^{(N,k)}}\},
\]
and the globally optimal minimum-error success probability is
\[
P_{N,k}
=\frac1N\left(\sum_{r=0}^{N-1}\sqrt{p_r^{(N,k)}}\right)^2.
\]
Thus the all-copy problem is the square of the Hellinger mass of a fair binomial random variable reduced modulo \(N\). When \(N>k\), no residue aliases and the formula reduces to
\[
P_{N,k}
=\frac1{N2^k}\left(\sum_{j=0}^k\sqrt{\binom{k}{j}}\right)^2,
\]
which recovers the previously derived non-aliasing expression. The formula above also covers every \(N\le k\), the regime explicitly left for separate investigation in the recent cyclic-geometrically-uniform analysis.

For each fixed \(N\), writing \(c_N=\cos(\pi/N)\), the exact formula yields the sharp error asymptotic
\[
1-P_{N,k}=\frac12c_N^{2k}+O(c_N^{3k}).
\]
Finally, among every fixed ensemble of \(N\) distinct pure real-qubit projective states, the regular polygon uniquely maximizes the multiple-Chernoff exponent, up to an orthogonal basis change and relabeling. The optimal exponent is
\[
-2\log\cos(\pi/N).
\]

## Assumptions and scope
The states are pure real qubits, equal priors are used, and discrimination is minimum-error with an unrestricted collective measurement on the \(k\) copies. Distinct real-qubit states are understood projectively, so angles are taken modulo \(\pi\). The exact finite-\(k\) formula is only asserted for the regular polygon. The final exponent statement concerns a fixed finite ensemble as the number of copies tends to infinity; it does not prove the stronger recent conjecture that the regular polygon maximizes the finite-copy success probability among all rebit ensembles for every \(N,k\).

All logarithms in the Chernoff exponent are natural logarithms. The \(O(\cdot)\) constant in the fixed-\(N\) expansion may depend on \(N\).

## Proof
Let \(G\) be the weighted Gram matrix,
\[
G_{ab}=\frac1N\langle\psi_a|\psi_b\rangle^k
=\frac1N\cos^k\!\left(\frac{\pi(a-b)}N\right).
\]
Using
\[
\cos^k t=2^{-k}\sum_{j=0}^k\binom{k}{j}e^{i(k-2j)t},
\]
define vectors \(v_j\in\mathbb C^N\) by
\[
(v_j)_a=e^{i(k-2j)\pi a/N}.
\]
Then
\[
G=\frac1{N2^k}\sum_{j=0}^k\binom{k}{j}v_jv_j^*.
\]
If \(j\equiv \ell\pmod N\), then \(v_j=v_\ell\). Otherwise
\[
\langle v_\ell,v_j\rangle
=\sum_{a=0}^{N-1}e^{2\pi i(\ell-j)a/N}=0.
\]
Because \(\|v_j\|^2=N\), grouping terms by the residue of \(j\) modulo \(N\) proves that the eigenvalue attached to residue \(r\) is exactly \(p_r^{(N,k)}\).

The ensemble is a pure geometrically uniform orbit, so its pretty-good measurement is minimum-error optimal. For an equiprobable pure GU orbit the diagonal entries of \(\sqrt G\) are equal; hence
\[
P_{N,k}
=\sum_{a=0}^{N-1}|(\sqrt G)_{aa}|^2
=\frac1N(\operatorname{tr}\sqrt G)^2,
\]
which gives the stated residue formula.

For the fixed-\(N\) asymptotic, the root-of-unity filter gives
\[
p_r^{(N,k)}
=\frac1N\sum_{\ell=0}^{N-1}
e^{-2\pi ir\ell/N}
\left(\frac{1+e^{2\pi i\ell/N}}2\right)^k.
\]
The modes \(\ell=1\) and \(\ell=N-1\) are the unique nonconstant modes of largest modulus \(c_N\), so
\[
p_r^{(N,k)}
=\frac1N\left[1+2c_N^k\cos\!\left(\frac{\pi k}N-\frac{2\pi r}N\right)+O(c_N^{3k})\right].
\]
For \(N\ge4\), the next Fourier modulus is at most \(|\cos(2\pi/N)|\le c_N^3\); for \(N=3\) there is no additional nonconstant mode. Expanding \(\sqrt{1+x}\), using exact cancellation of the first-order term after summing over \(r\), and
\[
\sum_{r=0}^{N-1}\cos^2\!\left(\frac{\pi k}N-\frac{2\pi r}N\right)=\frac N2,
\]
yields
\[
P_{N,k}=1-\frac12c_N^{2k}+O(c_N^{3k}).
\]

For the exponent statement, the multiple quantum Chernoff theorem says that the error exponent of any fixed finite pure-state ensemble is the minimum pairwise Chernoff distance. For pure states this is
\[
-\log|\langle\phi_i|\phi_j\rangle|^2.
\]
Represent \(N\) distinct real-qubit projective states by \(N\) points on the circle of length \(\pi\). Some adjacent projective angular gap is at most \(\pi/N\), so some pair has overlap at least \(\cos(\pi/N)\). Therefore every such ensemble has exponent at most \(-2\log\cos(\pi/N)\). Equality forces every cyclic gap to equal \(\pi/N\), which is precisely the regular polygon up to orthogonal rotation or reflection and relabeling. The exact finite-copy formula above shows that the regular polygon attains this exponent with the sharper prefactor \(1/2\).

## Verification
A standalone checker in `artifacts/verify.py` checks directly that the gauge-shifted cyclic characters are Gram eigenvectors with the claimed residue-sum eigenvalues for a grid of \((N,k)\) values. It also checks the stated fixed-\(N\) leading coefficient numerically at moderate copy numbers. These calculations corroborate, but do not replace, the analytic proof.

Boundary cases were checked symbolically in the proof: empty residue classes contribute zero eigenvalues; \(N>k\) removes all aliasing; and the \(N=3\) Fourier remainder contains no modes beyond the dominant conjugate pair.

## Relationship to prior work
Achenbach, Leppäjärvi, Lee, and Heinosaari (arXiv:2604.26647v1) introduce the same regular real-qubit cyclic ensemble, prove pure-GU PGM optimality in the setting used here, derive \(P=f(k)/N\) for \(N>k\), tabulate small \(k\), and explicitly state that the case \(N\le k\) needs separate investigation. Kvashchuk, Chernyshova, Porto, Ohst, Vieira, and Quintino (arXiv:2604.26927v1) independently give the non-aliasing regular-polygon value for \(N\ge k+1\), use it as a rebit lower bound, and conjecture finite-copy optimality of regular polygons more broadly.

Zhou, Chessa, Chitambar, and Leditzky (arXiv:2501.12376) and the earlier representation-theoretic treatment of Krovi, Guha, Dutton, and da Silva (arXiv:1507.04737) provide broader GU discrimination machinery and PGM optimality, but the inspected statements do not evaluate the symmetric-power regular-polygon spectrum as fair-binomial residue masses, do not supply the arbitrary-\(N,k\) aliasing formula, and do not give its sharp fixed-\(N\) prefactor. Ke Li's multiple Chernoff theorem (arXiv:1508.06624) supplies the general exponent theorem used in the last step; the new part there is the exact projective-circle extremal specialization linked to the same recent regular-polygon conjecture.

## Limitations
The finite-copy global conjecture remains open: this result computes the regular-polygon benchmark exactly but does not prove that no nonregular rebit ensemble can have larger \(P_{N,k}\) for a given finite \(k\). The uniqueness statement is for the asymptotic Chernoff exponent of a fixed ensemble; it does not exclude \(k\)-dependent families approaching the regular polygon. The work also does not address unequal priors, mixed states, local-measurement restrictions, or complex-qubit configurations.

A residual literature risk is that the binomial-residue specialization may have appeared under older phase-shift-keying or cyclic-frame terminology not retrieved in the targeted searches. The broader GU formulas were therefore treated as potentially dominating prior work and compared at the level of their stated implications rather than titles alone.

## References
1. T. Achenbach, L. Leppäjärvi, H. Lee, and T. Heinosaari, *Nonclassical traits in multi-copy state discrimination*, arXiv:2604.26647v1 (2026).
2. M. Kvashchuk, P. Chernyshova, L. E. A. Porto, T.-A. Ohst, L. B. Vieira, and M. T. Quintino, *The most discriminable quantum states in the multicopy regime*, arXiv:2604.26927v1 (2026).
3. J. Zhou, S. Chessa, E. Chitambar, and F. Leditzky, *On the distinguishability of geometrically uniform quantum states*, arXiv:2501.12376 (2025).
4. H. Krovi, S. Guha, Z. Dutton, and M. P. da Silva, *Optimal Measurements for Symmetric Quantum States with Applications to Optical Communication*, arXiv:1507.04737 (2015).
5. K. Li, *Discriminating quantum states: the multiple Chernoff distance*, arXiv:1508.06624 (2015).
