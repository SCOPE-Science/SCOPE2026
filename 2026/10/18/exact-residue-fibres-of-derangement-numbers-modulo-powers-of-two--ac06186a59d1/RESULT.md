# Exact residue fibres of derangement numbers modulo powers of two

## Finding

Let \(D_n\) be the number of fixed-point-free permutations of \(\{1,\ldots,n\}\), with \(D_0=1\). For every integer \(k\ge3\) and every residue \(a\pmod{2^k}\), the number of indices \(0\le n<2^k\) satisfying \(D_n\equiv a\pmod{2^k}\) equals

\[
N_k(a)=\begin{cases}
1,&a\equiv0\pmod2,\\
4,&a\equiv1\pmod8,\\
0,&\text{otherwise}.
\end{cases}
\]

Every indicated residue class occurs, and the image therefore has exactly \(5\cdot2^{k-3}\) members, or five eighths of the ambient residue classes. Since the sequence is periodic modulo \(2^k\), these counts also give ordinary natural densities \(N_k(a)/2^k\). Thus the even residue classes each have density \(2^{-k}\), the classes congruent to \(1\pmod8\) each have density \(2^{2-k}\), and all other classes have density zero.

The structural statement underlying the counts is an exact local \(2\)-adic isometry on odd indices and an exact valuation-shifted isometry on each of the two even-index branches modulo four; the assertion is not merely an enumeration of small moduli. The cases \(k=1,2\) have respective multiplicity profiles \((1,1)\) on residues \(0,1\), and \((1,2,1,0)\) on residues \(0,1,2,3\).

## Assumptions and scope

Throughout, \(\mathbb Z_2\) denotes the ring of \(2\)-adic integers, and \(\nu_2\) is the usual additive valuation with \(\nu_2(0)=+\infty\). The recurrence defining the classical derangement numbers is \(D_0=1\) and \(D_n=nD_{n-1}+(-1)^n\) for every integer \(n\ge1\). Define the signed sequence \(F(n)=(-1)^nD_n\), and its continuous \(2\)-adic extension

\[
F(x)=\sum_{j=0}^{\infty}(-1)^j P_j(x),\qquad
P_0(x)=1,\quad P_j(x)=\prod_{i=0}^{j-1}(x-i)\ (j\ge1).
\]

The infinite sum converges for every \(x\in\mathbb Z_2\), and on nonnegative integer arguments the terms after \(j=n\) vanish. This is the established falling-factorial interpolation, not itself claimed as novel. All residue assertions concern \(D_n\), rather than a generalized derangement sequence or a separate integer-valued function.

## Proof

**1. Uniform convergence and a congruence for increments.** In each block of \(j\) consecutive \(2\)-adic integers, at least \(\lfloor j/2\rfloor\) are even. Consequently \(P_j(x)\) is divisible by \(2^{\lfloor j/2\rfloor}\), uniformly for \(x\in\mathbb Z_2\). The formal derivative \(P'_j(x)\) is a sum of \(j\) products obtained by deleting one factor; each such product is divisible by \(2^{\lfloor j/2\rfloor-1}\) for \(j\ge2\). Thus \(F\) and the termwise formal derivative \(F'=\sum_{j\ge1}(-1)^jP'_j\) converge uniformly. Because \(P_j\) has integer coefficients, for all \(x,h\in\mathbb Z_2\) the polynomial difference \(P_j(x+h)-P_j(x)-hP'_j(x)\) belongs to \(h^2\mathbb Z_2\); taking limits gives

\[
F(x+h)-F(x)\equiv hF'(x)\pmod{h^2\mathbb Z_2}.
\tag{1}
\]

In particular \(F\) is \(1\)-Lipschitz, since each polynomial with integer coefficients is \(1\)-Lipschitz and this property survives uniform limits.

**2. Parity and the exact derivative valuations.** From the finite derangement recurrence we have \(F(n+1)=1-(n+1)F(n)\) for nonnegative integers. By density and continuity this identity holds for all \(x\in\mathbb Z_2\):

\[
F(x+1)=1-(x+1)F(x),\qquad
F'(x+1)=-F(x)-(x+1)F'(x).
\tag{2}
\]

The recurrence gives \(F(2u)\equiv1\pmod4\) and \(F(2u+1)\equiv0\pmod2\) for all nonnegative \(u\), hence throughout the corresponding \(2\)-adic parity classes. Directly differentiating at zero yields

\[
F'(0)=-\sum_{m=0}^{\infty}m!\equiv2\pmod4,
\tag{3}
\]

because only the terms through \(m=3\) contribute modulo four, and their sum is \(10\). Equation (2) now gives \(F'(x)\) odd when \(x\) is odd and even when \(x\) is even. More precisely, for \(u\ge1\),

\[
\frac{F'(2u)}2=-\frac{F(2u-1)}2-uF'(2u-1)\equiv-(1-u)-u\equiv1\pmod2,
\]

since \(F(2u-1)=1-(2u-1)F(2u-2)\equiv2-2u\pmod4\). The base \(u=0\) is (3). Continuity and density extend the result to all \(x\in\mathbb Z_2\):

\[
\nu_2(F'(x))=\begin{cases}0,&x\equiv1\pmod2,\\1,&x\equiv0\pmod2.\end{cases}
\tag{4}
\]

**3. Three isometric branches.** If \(x,y\in1+2\mathbb Z_2\) are distinct, put \(h=y-x\). Because \(\nu_2(h)\ge1\) and \(F'(x)\) is odd, the error \(h^2\mathbb Z_2\) in (1) has strictly greater valuation than its linear term. Hence

\[
\nu_2(F(x)-F(y))=\nu_2(x-y)\qquad(x,y\in1+2\mathbb Z_2).
\tag{5}
\]

Similarly, if \(x\equiv y\equiv0\pmod4\), or \(x\equiv y\equiv2\pmod4\), then \(\nu_2(h)\ge2\) and (4) imply

\[
\nu_2(F(x)-F(y))=\nu_2(x-y)+1.
\tag{6}
\]

In addition, \(F(x)\equiv1\pmod8\) for every even \(x\): indeed the recurrence (2) first gives, for integers \(u\ge1\), \(F(2u-1)\equiv2-2u\pmod4\), so \(F(2u)=1-2uF(2u-1)\equiv1-4u(1-u)\equiv1\pmod8\); continuity gives the general statement.

Therefore the following are well-defined isometries \(\mathbb Z_2\longrightarrow\mathbb Z_2\):

\[
H(t)=\frac{F(1+2t)}2,\qquad
G_0(t)=\frac{F(4t)-1}{8},\qquad
G_2(t)=\frac{F(2+4t)-1}{8}.
\tag{7}
\]

Equations (5) and (6) show in each case that the valuation of the difference of two outputs equals the valuation of the difference of their arguments. Every isometry of \(\mathbb Z_2\) into itself induces an injection on each finite quotient \(\mathbb Z/2^j\mathbb Z\); because the quotient has the same finite cardinality in the domain and codomain, this injection is a bijection. Passing to inverse limits proves that each of \(H,G_0,G_2\) is onto \(\mathbb Z_2\).

**4. Exact fibres modulo \(2^k\).** The odd indices \(n=1+2t\), with \(t\) running modulo \(2^{k-1}\), map through \(-2H(t)=D_n\) bijectively to all even residues modulo \(2^k\). They contribute exactly one index to each even residue. The even indices lie on the branches \(n=4t\) and \(n=2+4t\), for which \(D_n=1+8G_0(t)\) and \(D_n=1+8G_2(t)\). For \(k\ge3\), each branch produces every residue \(1\pmod8\) modulo \(2^k\) exactly twice among indices modulo \(2^k\), because its parameter runs modulo \(2^{k-2}\) and its output depends bijectively on the parameter modulo \(2^{k-3}\). Adding the two disjoint even branches gives multiplicity four; no other odd residues occur. These are all the indices modulo \(2^k\), proving the displayed formula.

Finally, the \(1\)-Lipschitz property gives \(F(n+2^k)\equiv F(n)\pmod{2^k}\). Since \(2^k\) is even, the same holds for \(D_n=(-1)^nF(n)\). Thus every block of \(2^k\) successive indices repeats, and division of exact per-period counts yields the asserted natural densities. The precise period \(2^k\) for the original derangement sequence is independently known from the earlier literature and is not claimed as new.

## Verification

The included standalone Python checker (`verify.py`, standard library only) computes \(D_n\pmod{2^k}\) from the integer recurrence and verifies the complete fibre profile for \(3\le k\le12\). It independently evaluates the derivative of truncated falling-factorial polynomials modulo eight on integer arguments, and checks the two exact local valuation laws on distinct finite index pairs. These finite tests detect computational or indexing errors but do not substitute for steps (1)--(7), which establish the statement for every \(k\ge3\).

## Relationship to prior work

Barsky proved \(p\)-adic local analytic interpolation for signed derangement numbers (1981, Proposition 5). Miska (arXiv:1508.01987, initially posted August 9, 2015, Sections 4.1.1--4.1.3) established the basic period modulo general integers and studied \(p\)-adic valuations and lifting of zeros. O'Desky and Richman (arXiv:2012.04615, Theorems 4.3 and 4.5) established a locally analytic \(p\)-adic interpolation using exactly the falling-factorial series underlying this proof. Ulas (*Fibonacci Quarterly* 61 (2023), Lemmas 2.1--2.2 and Theorem 2.3) proved the congruences modulo eight and precise valuations of classical derangement numbers, including the fact that even-index derangement numbers are \(1\pmod8\). In particular, the full \(k=3\) profile is already an immediate consequence of Ulas's Lemma 2.1; it is included only as the base case of the uniform all-exponents classification. These strong antecedents are not presented as new here.

The present classification is specifically the **complete image and exact multiplicity of every target residue modulo every power of two**, based on the three branchwise isometries and the resulting pushforward counting law. The periodicity, interpolation, the basic modulo-eight congruences, and previously established valuation formulas do not themselves state or numerically evaluate all those fibres. These antecedent statements do not themselves assert the complete all-exponents per-residue multiplicity law.

## Limitations

The result treats the ordinary derangement numbers, only the prime two, and moduli \(2^k\). It does not classify target fibres for odd prime powers, generalized derangements, or correlations of consecutive terms. The proof is mathematical and infinite; the checker covers only explicitly stated finite ranges. No assertion is made about a simultaneous distribution for multiple indices.

## References

1. Daniel Barsky, *Analyse p-adique et suites classiques de nombres*, Séminaire Lotharingien de Combinatoire B05b (1981), Proposition 5. https://www.mat.univie.ac.at/~slc/opapers/s05barsky.pdf
2. Piotr Miska, *Arithmetic properties of the sequence of derangements and its generalizations*, arXiv:1508.01987, first posted 2015-08-09, Sections 4.1.1--4.1.3. https://arxiv.org/abs/1508.01987
3. Andrew O'Desky and David H. Richman, *Derangements and the p-adic incomplete gamma function*, arXiv:2012.04615, Theorems 4.3 and 4.5. https://arxiv.org/abs/2012.04615
4. Maciej Ulas, *Representing generalized derangements as sums of three squares*, Fibonacci Quarterly 61 (2023), pp. 231--239, Section 2. https://www.fq.math.ca/Papers/61-3/ulas11202022.pdf
5. OEIS A000166, *Subfactorial or rencontres numbers*. https://oeis.org/A000166
