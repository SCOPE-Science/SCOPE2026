# Binomial dominance law and a six-point reversal in dicyclic groups

## Finding

Let \(G_n=\operatorname{Dic}_{4n}=\langle a,b\mid a^{2n}=1,\ b^2=a^n,\ bab^{-1}=a^{-1}\rangle\), of order \(4n\), and let \(A\) be uniformly chosen among its \(k\)-element subsets. Set \(\Delta(A)=|AA|-|AA^{-1}|\), where \(AA=\{xy:x,y\in A\}\) and \(AA^{-1}=\{xy^{-1}:x,y\in A\}\). For every fixed integer \(k\ge2\), the distribution of \(\Delta(A)\), as \(n\to\infty\), converges in total variation, with error \(O_k(n^{-1})\), to that of \(F_k(R)\), where \(R\sim\mathrm{Binomial}(k,1/2)\) and

\[
F_k(r)=\begin{cases}
\dfrac{r(3-r)}2,&0\le r<k,\\[4pt]
-\dfrac{(k-1)(k-2)}2,&r=k.
\end{cases}
\]

In particular, for each fixed \(k\ge4\), the fractions of product-dominant (more products than quotients), quotient-dominant, and balanced \(k\)-sets, respectively, are

\[
\begin{aligned}
P_k(n)&=\frac{k+\binom{k}{2}}{2^k}+O_k(n^{-1}),\\
Q_k(n)&=\frac{\sum_{r=4}^{k}\binom{k}{r}}{2^k}+O_k(n^{-1}),\\
B_k(n)&=\frac{1+\binom{k}{3}}{2^k}+O_k(n^{-1}).
\end{aligned}
\]

At the first reversal, \(k=6\), these three limiting proportions are \(21/64\), \(22/64\), and \(21/64\). Moreover, for every fixed \(k\ge6\), there are **strictly more quotient-dominant than product-dominant \(k\)-element subsets of \(G_n\) for all sufficiently large \(n\)**. This disproves Conjecture 6.1 of Mandal--Neetu (arXiv:2602.09073v1), which predicts the opposite eventual inequality for every fixed subset size. The statement is about *fixed-size subsets*, not the relative numbers of all subsets of the group.

## Assumptions and scope

Integers \(n\ge2\) tend to infinity while \(k\ge2\) is held fixed. The group is the dicyclic group with the above presentation; the quotient set is the right quotient set \(AA^{-1}\), not the left quotient set. Product-dominant means \(\Delta>0\), quotient-dominant means \(\Delta<0\), and balanced means \(\Delta=0\). All estimates \(O_k(\cdot)\) permit constants depending on the fixed value of \(k\), and make no claim of uniformity for \(k\) increasing with \(n\).

## Proof

**1. Normal forms and forced collisions.** Set \(N=2n\) and identify the normal form \(a^u b^e\), \(0\le u<N\), \(e\in\{0,1\}\), with \((u,e)\). Multiplication and inversion become

\[
(u,e)(v,f)=(u+(-1)^ev+nef\bmod N,\ e\oplus f),
\]
\[
(u,0)^{-1}=(-u,0),\qquad (u,1)^{-1}=(u+n,1).
\]

Write the rotation and outside elements of \(A\) as \(a^{u_1},\ldots,a^{u_r}\) and \(a^{v_1}b,\ldots,a^{v_s}b\), where \(r+s=k\). Treat the displayed exponents as formal independent variables when determining forced collisions.

The rotation-coset products in \(AA\) consist of the \(r(r+1)/2\) unordered rotation sums \(u_i+u_j\) (\(i\le j\)), together with the outside--outside expressions \(v_i-v_j+n\) for ordered pairs. In the latter family, all \(s\) diagonal expressions collapse to the single constant \(n\); the \(s(s-1)\) off-diagonal forms are otherwise distinct. The outside-coset products comprise the two families

\[
u_i+v_j\quad\text{and}\quad v_j-u_i,
\qquad 1\le i\le r,\ 1\le j\le s.
\]

Consequently, if \(s>0\) and there are no accidental modular coincidences, then

\[
|AA|=\frac{r(r+1)}2+\bigl(s(s-1)+1\bigr)+2rs.
\]

For \(s=0\), only the rotation sums remain and \(|AA|=k(k+1)/2\).

The rotation-coset elements of \(AA^{-1}\) are the two families \(u_i-u_j\) and \(v_i-v_j\); all diagonal pairs give the common identity. They therefore contribute \(1+r(r-1)+s(s-1)\) generic elements. The outside-coset quotients comprise

\[
u_i+v_j+n\quad\text{and}\quad u_i+v_j,
\qquad 1\le i\le r,\ 1\le j\le s.
\]

**The two quotients associated with each mixed pair differ by the nonzero central involution \(a^n\).** They are not identical, unlike in an ordinary dihedral group. Thus, apart from accidental coincidences,

\[
|AA^{-1}|=1+r(r-1)+s(s-1)+2rs=1+k(k-1).
\]

Subtracting gives \(\Delta=r(3-r)/2\) if \(s>0\), and \(\Delta=-(k-1)(k-2)/2\) if \(s=0\).

**2. Accidental collisions are rare.** Conditional on \(r,s\), the \(u_i\)'s and \(v_j\)'s are independently chosen as ordered samples without replacement from \(\mathbb Z/N\mathbb Z\) in their respective cosets. An equality between two expressions above, of the same coset parity, which is not one of the forced equalities in step 1, yields a nontrivial affine congruence

\[
\sum_i c_i u_i+\sum_j d_j v_j+\epsilon n\equiv0\pmod N,
\]

where each variable coefficient belongs to \(\{-2,-1,0,1,2\}\), and \(\epsilon\) is integral. Either at least one coefficient is nonzero, in which case conditioning on all other exponents leaves at most two solutions for that exponent modulo \(N\), or the variable coefficients are all zero and the remaining nontrivial constant is \(n\bmod N\), which cannot vanish. With at most \(k-1\) excluded residues in the relevant coset, any such coincidence has conditional probability at most \(2/(N-k+1)\) for \(N>k\). There are \(O(k^4)\) pairs of displayed forms. The union bound shows that all actual cardinalities equal their generic values outside an event of probability \(O_k(n^{-1})\).

**3. Coset sampling and limiting law.** Exactly \(2n\) of the \(4n\) elements are rotations. Hence

\[
\Pr\{r(A)=r\}=\frac{\binom{2n}{r}\binom{2n}{k-r}}{\binom{4n}{k}}
=\frac{\binom{k}{r}}{2^k}+O_k(n^{-1})
\]

for each \(0\le r\le k\). Combining with step 2 gives the asserted total-variation estimate and complete limiting discrepancy law.

For \(k\ge4\), the generic discrepancy is positive precisely for \(r\in\{1,2\}\), zero precisely for \(r\in\{0,3\}\), and negative precisely for \(4\le r\le k\); the last case includes the pure-rotation boundary \(r=k\). Summing binomial probabilities gives the three displayed fractions. At \(k=6\), product dominance has numerator \(\binom61+\binom62=21\), while quotient dominance has numerator \(\binom64+\binom65+\binom66=22\).

Finally, \(p_k=(k+\binom{k}{2})/2^k\) decreases strictly from \(k\ge3\), because \(p_{k+1}/p_k=(k+2)/(2k)<1\). The binomial tail \(q_k=\Pr\{\mathrm{Binomial}(k,1/2)\ge4\}\) increases strictly for \(k\ge3\), since \(q_{k+1}-q_k=\Pr\{\mathrm{Binomial}(k,1/2)=3\}/2>0\). The strict inequality \(q_6>p_6\) therefore persists for every \(k\ge6\). The \(O_k(n^{-1})\) error gives the eventual strict inequality of finite counts. \(\square\)

## Verification

The accompanying standalone `verify_sparse.py` executes exact normal-form group operations, symbolically enumerates forced affine word coincidences for every coset profile through size sixteen, exhaustively enumerates \(78{,}050\) small-group subsets, reproduces five published size-specific dicyclic enumeration table entries, and checks random large-order examples (recording rather than discarding incidental collisions). The expected output begins `VERIFY_OK`. The exact proof is the affine collision bound and binomial limit above, not this finite enumeration.

## Relationship to prior work

Mandal and Neetu (2026), Theorems 1.4 and 1.6, count dicyclic MSTD/MDTS subsets of sizes two and three; their Section 6 explicitly asks for size four and beyond and states Conjecture 6.1 of eventual MSTD prevalence at every fixed size. The present theorem gives the complete limiting law at every fixed size and contradicts that conjecture starting at six.

Amit et al. (2026) study product/quotient dominance of full power sets through moment criteria. Their Section 8 specifically identifies dicyclic groups as outside the scope of their main asymptotic conditions; full-power-set conclusions would not determine fixed-size fractions. Ascoli et al. (2022) prove eventual MSTD dominance for sparse subsets of generalized **dihedral** groups; their split extension has involutory outside elements, whereas here \(b^2=a^n\) causes the two mixed quotient families to remain separate. Thus their group-theoretic theorem does not encompass the present nonsplit case.

## Limitations

The theorem supplies a fixed-cardinality limit and an eventual reversal, not an explicit least \(n\) at which each inequality holds. It does not address the MSTD/MDTS difference after summing over all subset sizes, nor give an estimate uniform over growing \(k\). Small-group exhaustive examples and randomized experiments are checks of the formulas, not a substitute for the proof. Prior equivalent treatments in other terminology remain a literature risk.

## References

1. S. Mandal and Neetu, *Exact and Asymptotic Counts of MSTD, MDTS, and Balanced Sets in Dicyclic Groups*, arXiv:2602.09073v1, first public 2026-02-09, https://arxiv.org/html/2602.09073v1 (especially Theorems 1.4, 1.6 and Conjecture 6.1).
2. Y. Amit et al., *Product and Quotient Set Dominance in Finite Groups*, arXiv:2610.12912v1, first public 2026-10-09, https://arxiv.org/html/2610.12912v1 (especially Theorem 1.5 and Section 8).
3. R. Ascoli et al., *Sum and Difference Sets in Generalized Dihedral Groups*, arXiv:2210.00669, first public 2022-10-03, https://arxiv.org/abs/2210.00669 (Theorem 1.8; related split case only).
