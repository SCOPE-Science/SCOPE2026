# Valuation-uniform square-zero matrices over finite chain rings

## Finding

**Theorem (valuation spectrum and universality).** Let \(R\) be any finite commutative chain ring of length \(n\ge1\), with maximal ideal \((\pi)\), residue field \(R/(\pi)\) of cardinality \(q\), and \((\pi^n)=0\ne(\pi^{n-1})\). Set \(v(0)=n\), and for a nonzero element let \(v(a)\) be its unique ideal valuation in \(\{0,\ldots,n-1\}\). For a matrix \(A=(a_{ij})\in M_2(R)\), put \(v(A)=\min_{i,j}v(a_{ij})\). Define \(S_c=\{A\in M_2(R):A^2=0,\ v(A)=c\}\).

For every integer \(c\) with \(0\le c<n\),
\[
|S_c|=\begin{cases}
(q^2-1)q^{2n-2},&0\le 2c<n,\\[2pt]
q^{4(n-c)}-q^{4(n-c-1)},&n\le 2c<2n.
\end{cases}
\]
Moreover \(|S_n|=1\). In particular, **all valuation strata below half the ring length have equal cardinality**, regardless of the specific chain ring with parameters \((q,n)\).

The complete number of square-zero matrices is
\[
\boxed{\#\{A\in M_2(R):A^2=0\}=
\left(\left\lfloor\frac n2\right\rfloor+1\right)q^{2n}
-\left\lfloor\frac n2\right\rfloor q^{2n-2}.}
\]
Equivalently, writing the common count as \(N_n(q)\), and taking the harmless formal convention \(N_0(q)=1\), the length generating function is
\[
\boxed{\sum_{n\ge0}N_n(q)T^n=
\frac{1-q^2T^2}{(1-q^2T)^2(1+q^2T)}.}
\]
The generating function is a formal identity in \(\mathbb Q(q)[[T]]\); it enumerates rings of each length only insofar as their counts depend solely on \((q,n)\), not their numbers of isomorphism types.

## Assumptions and scope

A *finite commutative chain ring* is a finite nonzero commutative local ring whose ideals form a chain, equivalently whose maximal ideal is principal. The convention for length is \(R\supsetneq(\pi)\supsetneq\cdots\supsetneq(\pi^{n-1})\supsetneq(\pi^n)=0\). It includes fields (\(n=1\)), equal-characteristic truncations \(\mathbb F_q[t]/(t^n)\), and mixed-characteristic examples such as \(\mathbb Z/p^n\mathbb Z\). The residue field order \(q\) is a prime power. Each quotient \(R/(\pi^k)\), for \(1\le k\le n\), is itself a length-\(k\) chain ring of cardinality \(q^k\). Every ideal layer \((\pi^c)\) has size \(q^{n-c}\). No restriction on the characteristic or on \(q\) beyond the finite-chain-ring axioms is required.

## Proof

**Step 1: primitive square-zero matrices.** Call \(B\in M_2(S)\) *primitive* if one of its four entries is a unit, where \(S\) is a finite commutative chain ring of arbitrary positive length \(k\). Let \(B^2=0\). Its reduction \(\overline B\in M_2(\mathbb F_q)\) is nonzero and square-zero, hence has rank one. Choose a vector \(v\in S^2\) such that the reductions of \(Bv\) and \(v\) are independent over \(\mathbb F_q\); such a vector exists because a nonzero rank-one square-zero map in dimension two has its image equal to its kernel, and one may take a vector outside that line. By the local invertibility criterion, \((Bv,v)\) is a basis of \(S^2\). In that basis \(B(Bv)=0\) and \(B(v)=Bv\), so
\[
B\sim J=\begin{pmatrix}0&1\\0&0\end{pmatrix}
\quad\text{under }\operatorname{GL}_2(S).
\]
Conversely, every conjugate of \(J\) is primitive and square-zero. Its commuting invertible matrices are exactly
\[
\left\{\begin{pmatrix}a&b\\0&a\end{pmatrix}:a\in S^\times,\ b\in S\right\},
\]
with cardinality \(|S^\times||S|=(q-1)q^{2k-1}\). The reduction map \(\operatorname{GL}_2(S)\twoheadrightarrow\operatorname{GL}_2(\mathbb F_q)\) has kernel of cardinality \(q^{4(k-1)}\); thus
\[
|\operatorname{GL}_2(S)|=q^{4k-4}(q^2-1)(q^2-q).
\]
Orbit–stabilizer gives **the primitive square-zero count**
\[
P_k(q)=\frac{q^{4k-4}(q^2-1)(q^2-q)}{(q-1)q^{2k-1}}
=(q^2-1)q^{2k-2}.
\]
This argument also applies to \(k=1\).

**Step 2: the lower-valuation strata.** Fix \(0\le c<n\) with \(2c<n\). Multiplication by \(\pi^c\) identifies the additive groups \(R/(\pi^{n-c})\) and \((\pi^c)\), so every matrix with valuation exactly \(c\) has a unique representation \(A=\pi^cB\), where \(B\) is primitive over \(R/(\pi^{n-c})\). Its square vanishes in \(R\) precisely when the reduction of \(B\) to \(R/(\pi^{n-2c})\) is square-zero, since
\[
\pi^{2c}B^2=0\text{ in }R
\iff B^2=0\text{ in }R/(\pi^{n-2c}).
\]
This lower quotient has length \(n-2c\ge1\), and each of its four entries has \(q^c\) lifts to \(R/(\pi^{n-c})\). Reduction preserves primitivity. By Step 1,
\[
|S_c|=q^{4c}P_{n-2c}(q)
=q^{4c}(q^2-1)q^{2(n-2c)-2}
=(q^2-1)q^{2n-2}.
\]
The cancellation of \(c\) proves valuation uniformity.

**Step 3: upper-valuation strata.** If \(2c\ge n\), then every entry of a matrix in \((\pi^c)M_2(R)\) has product with every other such entry equal to zero, so every such matrix satisfies \(A^2=0\). Counting all four entries and subtracting the smaller ideal gives
\[
|S_c|=|\pi^cR|^4-|\pi^{c+1}R|^4
=q^{4(n-c)}-q^{4(n-c-1)}.
\]
The sole valuation-\(n\) matrix is zero.

**Step 4: summation and generating series.** There are exactly \(\lceil n/2\rceil\) values \(c\ge0\) with \(2c<n\). The strata from \(c=\lceil n/2\rceil\) through \(c=n\) sum by telescoping to \(q^{4\lfloor n/2\rfloor}\). Hence
\[
N_n(q)=q^{4\lfloor n/2\rfloor}
+\left\lceil\frac n2\right\rceil(q^2-1)q^{2n-2}.
\]
For \(n=2m\) and \(n=2m+1\), respectively, this equals
\[
(m+1)q^{4m}-mq^{4m-2},\qquad
(m+1)q^{4m+2}-mq^{4m},
\]
which is the claimed uniform floor-function formula. Summing the even and odd sequences as formal geometric series yields the displayed rational generating function. This finishes the proof.

## Verification

A standalone deterministic enumeration script, `checker.py`, tests matrix products directly, rather than deriving counts from the theorem. It exhausts the four matrix entries over the rings \(\mathbb Z/p^n\mathbb Z\) for \((p,n)\in\{(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(5,1),(5,2)\}\); all valuation strata and totals agree. It separately enumerates \(\mathbb F_4[t]/(t^n)\) for \(n\in\{1,2\}\), with finite-field multiplication implemented using \(u^2+u+1=0\); both agree. In particular, the valuation-vector counts including zero are \((192,192,240,15,1)\) over \(\mathbb Z/16\mathbb Z\) and \((240,255,1)\) over \(\mathbb F_4[t]/(t^2)\). The checker prints `VERIFY_OK` if all assertions hold.

The infinite family of results is established by the algebraic proof, not by extending finite experiments.

## Relationship to prior work

The finite-ring zero-square problem is motivated by the study of square-zero components in matrix decompositions, notably Danchev–García–Gómez Lozano, arXiv:2102.10460v1 (Theorem 2.6). That result establishes potent-plus-square-zero decompositions when the base ring has square-zero radical, rather than enumerating all square-zero matrices or their valuations over general chain rings. Cheraghpour–Ghosseiri, DOI:10.1080/03081087.2017.1418826 (Theorem 3.7 and Corollary 3.8), enumerate all *nilpotent* matrices over rings of the form \(\mathbb Z/m\mathbb Z\) but do not refine those counts by square-zero identity or valuation in the examined text. Carnevale–Shechter–Voll, arXiv:1709.02717v1, give a refined count for trace-zero matrices over DVR quotients, a different condition: a square-zero matrix over a nonreduced chain ring can have nonzero trace. Classical results on nilpotent matrices over \(\mathbb Z/m\mathbb Z\), including Ramirez–Bollman, DOI:10.1515/crll.1969.238.85, remain potentially relevant and are not claimed to be re-proved or superseded.

The asserted contribution is the **full valuation-stratified count for the equation \(A^2=0\) in two dimensions over arbitrary finite commutative chain rings**, including uniformity between distinct valuations and the length generating function. The elementary field-case orbit count is a prerequisite, not a separate novelty claim.

## Limitations

The theorem concerns only \(2\times2\) matrices, square-zero index at most two, and commutative chain rings; neither higher matrix dimension nor arbitrary non-chain local rings is addressed. The formula concerns counts, not complete conjugacy classification of all nonprimitive matrices. The 1969 Ramirez–Bollman paper was located bibliographically but its full text was not accessed, so equivalent earlier coverage of special instances cannot be ruled out. Numerical enumeration is restricted to the small stated examples. No claim of independent review is made.

## References

1. P. Danchev, E. García, M. Gómez Lozano, *Decompositions of Matrices into Potent and Square-Zero Matrices*, arXiv:2102.10460v1 (first public version 2021-02-20), Theorem 2.6. https://arxiv.org/abs/2102.10460
2. H. Cheraghpour, N. M. Ghosseiri, *On the idempotents, nilpotents, units and zero-divisors of finite rings*, Linear and Multilinear Algebra 67 (2019), 327–336, DOI:10.1080/03081087.2017.1418826, Theorem 3.7 and Corollary 3.8.
3. A. Carnevale, S. Shechter, C. Voll, *Enumerating traceless matrices over compact discrete valuation rings*, arXiv:1709.02717 (first public version 2017-09-08). https://arxiv.org/abs/1709.02717
4. H. Ramirez, D. Bollman, *On the number of nilpotent matrices over Zm*, Journal für die reine und angewandte Mathematik 238 (1969), 85–88, DOI:10.1515/crll.1969.238.85 (bibliographic record only).
