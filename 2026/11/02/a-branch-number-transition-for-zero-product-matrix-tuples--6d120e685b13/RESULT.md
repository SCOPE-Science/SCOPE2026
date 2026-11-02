# A branch-number transition for zero-product matrix tuples

## Finding

For a field \(K\) and integers \(m,n\geq1\), let \(X_{m,n}(K)\) be the set of ordered \(m\)-tuples \((A_1,\ldots,A_m)\) of \(n\times n\) matrices satisfying \(A_iA_j=0\) whenever \(i\ne j\). Write \(S=\sum_i A_i\), and let \(U_{m,n}\) be the locus where \(S\) is invertible. **The zero-product unit-sum and branch-transition theorem** consists of the following connected statements.

1. For every weak composition \(\mathbf r=(r_1,\ldots,r_m)\) of \(n\), the rank stratum \(U_{m,n}(\mathbf r)\) is a smooth geometrically irreducible variety of dimension \(n^2\). For every finite field \(\mathbb F_q\), its number of rational points is exactly \(|\mathrm{GL}_n(q)|\), independently of \(\mathbf r\). Thus
   \[
   |U_{m,n}(\mathbb F_q)|=\binom{n+m-1}{m-1}|\mathrm{GL}_n(q)|.
   \]
   Over any field \(K\), the motivic identity in the Grothendieck ring of varieties is \([U_{m,n}]=\binom{n+m-1}{m-1}[\mathrm{GL}_n]\). In particular, conditional on invertibility of \(S\), the rank vector is **exactly uniform over all weak compositions**, for every prime power \(q\).
2. For fixed \(n\geq2\), the proportion of the full pair variety \(X_{2,n}(\mathbb F_q)\) with invertible sum is \(1-O_n(q^{-1})\) as \(q\to\infty\) through prime powers. By contrast, for every fixed \(n\geq2\) and \(m\geq4\), this proportion is \(O_{m,n}(q^{-\delta_{m,n}})\), where
   \[
   \delta_{m,n}=(m+1)\left\lfloor\frac{n^2}{4}\right\rfloor-n^2>0.
   \]
3. At the intervening three-branch case, if \(n\geq2\) is even and \(C_n=\binom{n+2}{2}\), then
   \[
   \limsup_{q\to\infty}\frac{|U_{3,n}(\mathbb F_q)|}{|X_{3,n}(\mathbb F_q)|}\leq\frac{C_n}{C_n+1}<1.
   \]
   No asymptotic claim is made here for odd \(n\geq3\) at three branches.
4. In the first nontrivial dimension \(n=2\), the full \(m\)-branch count is exactly
   \[
   |X_{m,2}(\mathbb F_q)|=\binom{m+1}{2}|\mathrm{GL}_2(q)|+1+(q+1)(q^m-1)+m q(q^2-1).
   \]
   Consequently, at \(n=2\) the invertible-sum probability tends to \(1\) for \(m=2\), to \(6/7\) for \(m=3\), and is asymptotic to \(\binom{m+1}{2}q^{3-m}\) for every fixed \(m\geq4\).

## Assumptions and scope

The products \(A_iA_j=0\) are imposed only for **distinct** indices; no condition \(A_i^2=0\) is imposed on an individual matrix. The tuple is ordered, zero matrices are permitted, and all matrix ranks are ordinary vector-space ranks. The finite-field asymptotics keep \(n,m\) fixed while \(q\) increases through prime powers. The assertion concerning varieties is about the unit-sum locus with its naturally induced scheme structure. The Grothendieck-ring assertion holds over any base field; it does not assert that each stratum is isomorphic to \(\mathrm{GL}_n\) as a variety.

## Proof

**1. Normalize on the unit-sum locus.** Distinct-index zero products imply that all \(A_i\) commute with \(S\), and \(A_iS=A_i^2\). When \(S\) is invertible, define \(E_i=A_iS^{-1}\). Then
\[
E_i^2=A_i^2S^{-2}=A_iSS^{-2}=E_i,\quad E_iE_j=0\ (i\ne j),\quad\sum_iE_i=I_n.
\]
Conversely, given an ordered direct-sum decomposition \(K^n=V_1\oplus\cdots\oplus V_m\) (zero summands allowed), choose independently \(T_i\in\mathrm{GL}(V_i)\). Extending \(T_i\) by zero on the other summands yields \(A_i\) with all cross products zero and \(S=\bigoplus_iT_i\) invertible. The two constructions are inverse. Thus the rank vector of the \(A_i\) is precisely the dimension vector \(\dim V_i\), and it sums to \(n\).

**2. Count and identify the geometry.** For a fixed composition \(\mathbf r\), set \(G=\mathrm{GL}_n\) and \(H=\prod_i\mathrm{GL}_{r_i}\). The variety of ordered decompositions is \(G/H\). The independent automorphisms on the summands form an associated \(H\)-bundle with fiber \(H\), with conjugation transition action. It is Zariski locally trivial because the tautological summand bundles are locally trivial. Its total space is \(U_{m,n}(\mathbf r)\). Therefore this stratum is smooth and geometrically irreducible, with dimension \((n^2-\sum_i r_i^2)+\sum_i r_i^2=n^2\). For finite fields, there are \(|G(\mathbb F_q)|/|H(\mathbb F_q)|\) decompositions and \(|H(\mathbb F_q)|\) invertible-block choices, giving exactly \(|G(\mathbb F_q)|\). The same locally trivial bundle calculation gives \([U_{m,n}(\mathbf r)]=[G/H][H]=[G]\) in \(K_0(\mathrm{Var}_K)\). The rank strata are disjoint open-and-closed subvarieties of \(U_{m,n}\), since the ranks of a complete orthogonal idempotent family are locally constant. Stars-and-bars supplies \(\binom{n+m-1}{m-1}\) strata.

**3. Two branches.** For \(m=2\), fix \(r=\mathrm{rank}(A_1)\). The condition \(A_1A_2=A_2A_1=0\) says exactly that \(A_2\) factors as a map \(K^n/\mathrm{im}(A_1)\to\ker(A_1)\), between two spaces of dimension \(n-r\). Consequently the number of tuples with ranks \((r,s)\) is
\[
{n\brack r}_q^2|\mathrm{GL}_r(q)|\,{n-r\brack s}_q^2|\mathrm{GL}_s(q)|,\qquad 0\leq r+s\leq n.
\]
Here \({a\brack b}_q\) is a Gaussian binomial coefficient and \(|\mathrm{GL}_0(q)|=1\). This polynomial has degree \(n^2-(n-r-s)^2\) with leading coefficient one. Exactly the \(n+1\) cases \(r+s=n\) have degree \(n^2\), giving \(|X_{2,n}|=(n+1)q^{n^2}+O_n(q^{n^2-1})\). Meanwhile \(|U_{2,n}|=(n+1)|\mathrm{GL}_n(q)|=(n+1)q^{n^2}(1+O_n(q^{-1}))\); division proves the stated probability.

**4. Competing square-zero locus.** Let \(t=\lfloor n/2\rfloor\), \(s=n-t\), and choose a \(t\)-dimensional subspace \(W\subset\mathbb F_q^n\). Consider \(m\)-tuples in which every matrix kills \(W\) and maps \(\mathbb F_q^n/W\) into \(W\). Then all products, including squares, vanish and in particular \(S^2=0\). Restrict to tuples with aggregate image equal to \(W\) and common kernel equal to \(W\); these recover \(W\) uniquely, so the families indexed by different \(W\) are disjoint. For fixed \(n\geq2,m\geq3\), a proportion \(1-O_{m,n}(q^{-1})\) of all \(m\)-tuples of maps from an \(s\)-space to a \(t\)-space satisfy these two rank conditions. Indeed both are nonempty determinant-open conditions: the horizontal concatenation has full row rank \(t\), and the vertical stacking has full column rank \(s\); for \(s\in\{t,t+1\}\) and \(m\geq3\) these conditions have a simultaneous realization. Failure of each selected nonzero minor has probability \(O(q^{-1})\). There are \({n\brack t}_q=q^{ts}(1+O_n(q^{-1}))\) choices of \(W\), and \(q^{mts}\) unrestricted maps. The resulting *distinct* nonunit-sum tuples therefore number
\[
q^{(m+1)ts}(1-O_{m,n}(q^{-1})).
\]
If \(m\geq4\), the exponent exceeds \(n^2\) by \(\delta_{m,n}>0\); comparing to \(|U_{m,n}|=\binom{n+m-1}{m-1}|\mathrm{GL}_n(q)|=O(q^{n^2})\) proves the claimed decay. If \(m=3\) and \(n=2t\), the square-zero subfamily has \(q^{n^2}(1+O(q^{-1}))\) elements and is disjoint from the \(C_nq^{n^2}(1+O(q^{-1}))\) unit-sum tuples. This yields the strict limsup upper bound. For odd \(n\), the constructed family alone gives a lower-dimensional subset and no claimed decision of the critical case.

**5. Complete dimension-two enumeration.** Every nonzero singular \(2\times2\) matrix has rank one. A rank-one nilpotent \(A\) has equal image and kernel, a line \(L\). Any nonzero \(B\) with \(AB=BA=0\) has the same image and kernel, and therefore is a scalar multiple of a fixed nonzero map \(\mathbb F_q^2/L\to L\). For each of the \(q+1\) lines, this gives \(q^m-1\) nonzero ordered tuples of mutually annihilating nilpotents, all with noninvertible sum, with no double counting. If no nonzero constituent is nilpotent, all nonzero constituents have rank one with distinct image and kernel. Any two such matrices that annihilate each other act invertibly on complementary lines, and a third cannot be nonzero; thus their sum is invertible when two are present. The remaining nonunit-sum tuples consist of the all-zero tuple and tuples with exactly one nonzero nonnilpotent rank-one matrix. The latter matrix count is \((q-1)(q+1)^2-(q^2-1)=q(q^2-1)\), giving \(m q(q^2-1)\) choices. Adding the universal unit-sum count proves the exact expression and all claimed asymptotic cases.

## Verification

The accompanying `verify_annihilation_phase.py` enumerates matrices over prime fields and directly computes every ordered zero-product tuple for \(n=2,q=2\) and \(m=1,2,3,4,5\); \(n=2,q=3\) and \(m=1,2,3\); and \(n=3,q=2,m=2\). It checks the full dimension-two count where applicable, every invertible-sum rank composition, and the universal unit-sum count. All nine cases returned `PASS`, followed by `VERIFY_OK`. This is a finite check, not an infinite-field proof. The arguments in the preceding section establish the results for all fields and stated parameters.

## Relationship to prior work

Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity* (arXiv:2110.15566, first posted 2021-10-29), gives a generating function for **all pairs** of zero-product matrices. Its §3.1 fixes one matrix and counts the other via the induced map between quotient and kernel. The two-branch formula used here is a rank refinement of that standard argument; no priority is claimed for it. The contribution here concerns the arbitrary number of branches, the *unit-sum* rank-uniform geometry and motivic identity, the sharp higher-branch asymptotic contrast, and the exact first-dimensional all-branch census. Prior classifications of **nilpotent pairs** by Schröer, Oblak, and Bondarenko–Gerasimova–Sergeichuk concern related but different slices; they do not in their inspected statements furnish the combined higher-branch conclusion. General work on module-variety stratifications provides background but does not by itself certify publication priority for these formulas.

## Limitations

The theorem does not determine the total number of tuples for arbitrary \(n\geq3,m\geq3\). For \(m=3\) and odd \(n\geq3\) it makes no generic-probability assertion. The higher-branch estimate is a one-sided bound, not a sharp full count of nonunit tuples or their irreducible components. An equivalent general count could be implicit in the literature on representation varieties of ordinary multiple-point curve singularities or orthogonal-idempotent bundles; the originality comparison is limited to the sources described here. Independent mathematical validation has not been performed.

## References

1. Y. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, arXiv:2110.15566 (first posted 2021-10-29), https://arxiv.org/html/2110.15566v3.
2. J. Schröer, *Varieties of pairs of nilpotent matrices annihilating each other*, Commentarii Mathematici Helvetici 79 (2004), 396–426, https://ems.press/journals/cmh/articles/439.
3. P. Oblak, *Jordan forms for mutually annihilating nilpotent pairs*, arXiv:math/0612300, https://arxiv.org/abs/math/0612300.
4. V. M. Bondarenko, T. G. Gerasimova, V. V. Sergeichuk, *Pairs of mutually annihilating operators*, Linear Algebra and its Applications 430 (2009), 86–105, https://arxiv.org/abs/0812.2155.
5. N. J. Richmond, *A Stratification for Varieties of Modules*, Bulletin of the London Mathematical Society 33 (2001), 565–577, https://doi.org/10.1112/S0024609301008189.
