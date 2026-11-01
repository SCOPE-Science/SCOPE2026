# A sharp three-basis support law for the seven-point Fourier and quadratic-chirp transforms

## Finding

Let \(\omega=e^{2\pi i/7}\), and for every nonzero function \(f:\mathbb Z/7\mathbb Z\to\mathbb C\) define
\[
(\mathcal Ff)(k)=\sum_{j=0}^{6}\omega^{kj}f(j),\qquad
(\mathcal Cf)(k)=\sum_{j=0}^{6}\omega^{kj-j^2}f(j).
\]
With support always counted among the seven indices, the exact sharp inequality is
\[
\boxed{|\operatorname{supp}f|+|\operatorname{supp}\mathcal Ff|+|\operatorname{supp}\mathcal Cf|\ge 14.}
\]
Equality is attained by \(f=\delta_0-\delta_1\), whose three support sizes are \((2,6,6)\). This concerns the specifically defined computational, Fourier and quadratic-chirp bases; the unnormalized transforms have the same zero sets as their normalized unitary versions. The three bases are mutually unbiased.

## Assumptions and scope

Indices and all polynomial exponents in the definitions are interpreted modulo \(7\). The coefficient field of \(f\) is the entire complex field: no restrictions on phases, amplitudes, or sparsity are imposed beyond \(f\ne0\). For a seven-vector \(v\), write \(|\operatorname{supp}v|=|\{j:v_j\ne0\}|\). Multiplying either transformed vector by \(1/\sqrt7\) does not alter support.

The mutual unbiasedness of the three bases follows from orthogonality of the Fourier matrix and from the standard quadratic Gauss-sum identity: the modulus of \(\sum_{j=0}^6\omega^{u j^2+v j}\) is \(\sqrt7\) whenever \(u\not\equiv0\pmod7\).

## Proof

Write \(s=|\operatorname{supp}f|\) and \(S=\operatorname{supp}f\). Set \(a=7-|\operatorname{supp}\mathcal Ff|\) and \(b=7-|\operatorname{supp}\mathcal Cf|\). By the prime-order Fourier support theorem (equivalently, nonvanishing of all Fourier minors), the two inequalities
\[
|\operatorname{supp}\mathcal Ff|\ge8-s,\qquad
|\operatorname{supp}\mathcal Cf|\ge8-s
\]
hold, since chirp multiplication \(j\mapsto\omega^{-j^2}f(j)\) preserves \(s\). Thus \(0\le a,b\le s-1\).

Suppose the claimed inequality fails. Then \(s+(7-a)+(7-b)\le13\), so \(a+b\ge s+1\). Choose \(U\) among the Fourier zeros and \(V\) among the chirped-Fourier zeros with \(|U|+|V|=s+1\). Such subsets exist with \(|U|,|V|\le s-1\): choose any \(s+1\) of the \(a+b\) available zeros.

The nonzero coefficient vector \((f(j))_{j\in S}\) lies in the kernel of the \((s+1)\)-by-\(s\) matrix
\[
M(S,U,V)=
\begin{pmatrix}
(\omega^{kj})_{k\in U,\,j\in S}\\
(\omega^{kj-j^2})_{k\in V,\,j\in S}
\end{pmatrix}.
\]
We now give an **exact, exhaustive finite certificate** that every such matrix has column rank \(s\) over \(\mathbb C\). Work modulo the prime \(1009\). The residue \(105\) has order exactly \(7\) modulo \(1009\), hence evaluation \(\omega\mapsto105\) defines a ring homomorphism from \(\mathbb Z[\omega]\) to \(\mathbb F_{1009}\). If any specialized matrix has full column rank, one of its \(s\)-by-\(s\) minors is nonzero modulo \(1009\); that same cyclotomic-integer minor must be nonzero over \(\mathbb C\). **Only this one-way implication is used.**

For each \(s\in\{1,\ldots,7\}\), each \(S\subseteq\{0,\ldots,6\}\) of size \(s\), and each \(U,V\) with \(|U|+|V|=s+1\) and \(|U|,|V|\le s-1\), the standalone exact-integer checker performs Gaussian elimination modulo \(1009\). The numbers of full-column-rank matrices by \(s=1,\ldots,7\) are respectively
\[
(0,\ 0,\ 15435,\ 51450,\ 56595,\ 23324,\ 2989),
\]
with **zero rank-deficient instances** in all \(149793\) cases. The zero counts at \(s=1,2\) mean no admissible pairs \((U,V)\), not failed tests. The checker enumerates every subset combination without sampling. This contradicts the existence of a nonzero kernel vector, proving the lower bound for every complex \(f\).

Finally, for \(f=\delta_0-\delta_1\), the transforms are \((\mathcal Ff)(k)=1-\omega^k\) and \((\mathcal Cf)(k)=1-\omega^{k-1}\). Each has one zero, at \(k=0\) and \(k=1\) respectively, so the three support sizes are exactly \((2,6,6)\). Sharpness follows.

## Verification

The complete executable certificate is the standalone file `CHECK.py`; it requires Python 3.9 or newer and only standard-library modules. Execute `python3 CHECK.py`. Its direct checks include primality of \(1009\), the order-seven property of \(105\), exact finite-field rank elimination in all \(149793\) cases, the predicted enumeration counts, and the sharp example. A separate compiled exact-integer enumeration using a different elimination implementation independently reproduced the same seven counts. Neither floating-point arithmetic nor a probabilistic rank heuristic is involved. The exhaustive modular certificate proves the needed characteristic-zero ranks by specialization; it does not claim a classification of every equality case.

## Relationship to prior work

Tao's prime-cyclic uncertainty theorem gives the pairwise lower bound \(s+|\operatorname{supp}\mathcal Ff|\ge8\), and the same for \(\mathcal C\). Fiorentino and Weigert (2022) establish these bounds for pairs from standard mutually unbiased bases and give the general three-basis estimate \(\ge12\), together with results for the complete **eight**-basis family. Their article identifies sharp support bounds for smaller families such as triples as a separate direction in its conclusion. Its numerical observations about particular seven-dimensional triple zero patterns do not furnish the present exhaustive exact lower bound \(14\). The new statement concerns three explicit bases, not the complete eight-basis sum.

## Limitations

The conclusion is confined to the displayed triple in dimension seven. It does not classify all equality vectors, other choices of three bases, other dimensions, or approximate sparsity under perturbation. The finite-field certificate is complete only for the precisely stated rank predicate, not an exhaustive survey of all properties of these bases. Historical priority beyond the inspected literature remains subject to independent verification; no independent mathematical audit has been performed.

## References

1. V. Fiorentino and S. Weigert, *Uncertainty relations for the support of quantum states*, arXiv:2209.09817, first version September 20, 2022; *Journal of Physics A: Mathematical and Theoretical* 55 (2022), 495305, DOI: 10.1088/1751-8121/aca9a4. https://arxiv.org/abs/2209.09817 . The publicly available full article is https://eprints.whiterose.ac.uk/id/eprint/194248/7/Fiorentino_2022_J._Phys._A_Math._Theor._55_495305.pdf . In particular see §§2.2, 3.1–3.2, 4.3–4.4, 5.3 and 6.
2. T. Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286, first version August 29, 2003; *Mathematical Research Letters* 12 (2005), 121–127. https://arxiv.org/abs/math/0308286 .
