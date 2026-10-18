# Sharp first-moment sign transition for dicyclic product–quotient sets

## Finding

Let \(n\ge2\) be an integer and let
\[
D_n=\langle a,b\mid a^{2n}=1,\ b^2=a^n,\ bab^{-1}=a^{-1}\rangle,
\qquad |D_n|=4n.
\]
This notation means the order-\(4n\) dicyclic group; it is sometimes denoted \(\operatorname{Dic}_{4n}\). For \(A\subseteq D_n\) put
\[
\Delta(A)=|AA|-|AA^{-1}|,\qquad M(n)=\sum_{A\subseteq D_n}\Delta(A).
\]
Write \(L_1=1\), \(L_2=3\), and \(L_{m+2}=L_{m+1}+L_m\) for the Lucas sequence. For \(0\le j<2n\) define
\[
d_j=\gcd(2n,j),\quad e_j=\gcd(2n,n-j),\quad
\epsilon_j=\begin{cases}1&j\equiv0\pmod2,\\0&j\equiv1\pmod2.\end{cases}
\]
Then the exact first moment is
\[
\boxed{M(n)=\sum_{j=0}^{2n-1}\left(
L_{2n/d_j}^{\,2d_j}-3^{\,n-\epsilon_j}L_{2n/e_j}^{\,e_j}
\right)-4n\,7^{n-1}.}
\]
Its sign has a sharp, exhaustive phase transition:
\[
\boxed{M(n)<0\quad(2\le n\le29),\qquad M(n)>0\quad(n\ge30).}
\]
In particular, \(M(29)=-203011530049362987071455440\) and \(M(30)=397569666293094423242677920\). There are no zero cases in the stated domain.

## Assumptions and scope

All subsets, including the empty subset, are included in the raw sum. The quotient set is the **right** quotient set \(AA^{-1}=\{xy^{-1}:x,y\in A\}\), not \(A^{-1}A\). The group parameter is any integer \(n\ge2\), with no parity or primality restriction. The assertion concerns the sign of the **first raw moment**. It does not equate that sign with a comparison of the numbers of product-dominant and quotient-dominant subsets; such a conclusion needs additional hypotheses.

## Proof

**Independent-set reduction.** For a fixed \(g\in D_n\), put \(P_g(x)=x^{-1}g\) and \(Q_g(x)=gx\). These are permutations of the \(4n\) group elements. The condition \(g\notin AA\) is equivalent to never selecting both \(x\) and \(P_g(x)\), and \(g\notin AA^{-1}\) is equivalent to never selecting both \(x\) and \(Q_g(x)\). A permutation cycle of length \(m\) has exactly \(L_m\) such independent subsets, including for \(m=1\), when its single element is forbidden. Different cycles contribute independently. Denote these two avoidance counts by \(I_P(g)\) and \(I_Q(g)\). Since \(|AA|=\sum_g(1-\mathbf1_{g\notin AA})\), summing over all subsets proves
\[
M(n)=\sum_{g\in D_n}\bigl(I_Q(g)-I_P(g)\bigr).
\]

**Cycle decomposition.** Represent elements as \((i,t)=a^ib^t\) with \(0\le i<2n\) and \(t\in\{0,1\}\). Their exact multiplication is
\[
(i,t)(j,u)=(i+(-1)^tj+ntu\pmod{2n},\ t+u\pmod2).
\]
For \(g=a^j\), left multiplication \(Q_g\) has \(2d_j\) cycles, each of length \(2n/d_j\); therefore \(I_Q(a^j)=L_{2n/d_j}^{2d_j}\). The permutation \(P_g\) restricts on the rotation coset to \(i\mapsto j-i\). It has two fixed points when \(j\) is even and none otherwise, leaving \(n-\epsilon_j\) transpositions and a factor \(3^{n-\epsilon_j}\). On the other coset it is the translation \(i\mapsto i+n-j\), with \(e_j\) cycles of length \(2n/e_j\). Thus
\[
I_P(a^j)=3^{n-\epsilon_j}L_{2n/e_j}^{e_j}.
\]
For \(g=a^jb\), left multiplication has order \(4\), hence \(n\) four-cycles and \(I_Q(g)=7^n\). The permutation \(P_g\) exchanges the two cosets and has exactly two two-cycles and \(n-1\) four-cycles (its square fixes precisely the four elements with rotation index \(0\) or \(n\)). Consequently \(I_P(g)=3^2 7^{n-1}\) and \(I_Q(g)-I_P(g)=-2\cdot7^{n-1}\). There are \(2n\) such elements; substituting the two cases proves the exact formula.

**Uniform positivity above a finite cutoff.** Set \(\lambda=7^{1/4}\). For every integer \(m\ge3\), induction from \(L_3=4<\lambda^3\), \(L_4=7=\lambda^4\), and \(\lambda^2>\lambda+1\) proves \(L_m\le\lambda^m\). The latter strict inequality follows algebraically from \(8>3\sqrt7\), itself equivalent to \(64>63\). In the formula, the quotient-avoidance term with \(j=n\) is exactly \(9^n\). The product-avoidance term with \(j=0\) is exactly \(9^n/3\); the term with \(j=n\) is at most \(3^n\). For every other \(j\), the Lucas index \(2n/e_j\) is at least \(3\), so the corresponding product-avoidance term is at most
\[
3^n 7^{n/2}=(3\sqrt7)^n<8^n.
\]
All omitted quotient-avoidance terms are nonnegative. It follows rigorously that
\[
M(n)\ge B(n):=\tfrac23\,9^n-3^n-(2n-2)8^n-4n7^{n-1}.
\]
Exact integer arithmetic gives
\[
3B(41)=105308709116820901835784452756627203197>0.
\]
Moreover,
\[
\frac{B(n)}{9^n}=\frac23-3^{-n}-(2n-2)(8/9)^n-\frac{4n}{7}(7/9)^n.
\]
Each of the three subtracted positive quantities decreases strictly for integer \(n\ge41\). Therefore \(B(n)>0\), and hence \(M(n)>0\), for all \(n\ge41\).

**Remaining finite range.** For every integer \(2\le n\le40\), the attached complete exact-integer script `verify.py` evaluates the proved formula, tests strict negativity at every \(2\le n\le29\) and strict positivity at every \(30\le n\le40\), and checks the two boundary values displayed above. Thus no parameter is omitted: the finite computation handles \(2\le n\le40\), while the preceding inequality handles \(n\ge41\). Together they prove the sharp sign theorem.

## Verification

Run `python3 verify.py` in a directory containing that file. It requires only Python 3 and its standard library. Besides recomputing the complete finite interval with arbitrary-precision integers, it independently generates the permutations \(P_g\) and \(Q_g\) from the group law for every \(2\le n\le15\), and directly enumerates all \(2^{4n}\) subsets for \(n=2,3,4\). The script also verifies the exact inequality at \(n=41\). All of these checks were executed successfully from the supplied file. The induction and monotonicity argument, not finite tests, prove the infinite range.

## Relationship to prior work

Amit, Chen, Housholder, Im, Khan, Miller, Palomares, and Pradhan (2026, arXiv:2610.12912v1) express first moments through forbiddance-graph cycles and group characters (notably Theorem 7.6). They explicitly identify dicyclic groups as a family whose first moments and lower-order terms require further analysis (Sections 1.2 and 8). That general formula permits group-specific evaluation but does not give the exact parameter-wide sign transition established here. The present proof avoids a character table by using the two cosets and their explicit permutation cycles.

Mandal and Neetu (2026, arXiv:2602.09073v1) count product-/quotient-dominant and balanced dicyclic subsets of cardinalities two and three, and give bounds for a restricted half-size family. Their statements neither sum the discrepancy over every subset cardinality nor imply the raw first-moment threshold. Miller and Vissuet (2014) show that most subsets of large groups are balanced, but this asymptotic assertion does not determine the sign of the small unbalanced contribution to the mean.

## Limitations

The result does not decide whether \(D_n\) has more product-dominant than quotient-dominant subsets for any particular \(n\). A sign of the mean alone cannot decide that counting comparison. It does not determine the second moment, prove the moment-ratio hypothesis in the cited criterion, or count extremal subsets. The finite arithmetic check is executable rather than a separately formalized proof; its domain is bounded and precisely specified. Novelty was compared against the identified primary results and a targeted mathematical-results index, but unindexed earlier computations remain possible. No independent external audit has been performed.

## References

1. Yuval Amit, Lucas Chen, Christopher Housholder, Joshua Im, Joshua Khan, Steven J. Miller, Mateo Palomares, and Devayani Pradhan, *Product and Quotient Set Dominance in Finite Groups*, arXiv:2610.12912v1 (first public 2026-10-09), https://arxiv.org/abs/2610.12912.
2. Sagar Mandal and Neetu, *Exact and Asymptotic Counts of MSTD, MDTS, and Balanced Sets in Dicyclic Groups*, arXiv:2602.09073v1 (2026), https://arxiv.org/abs/2602.09073.
3. Steven J. Miller and Kevin Vissuet, *Most Subsets Are Balanced in Finite Groups*, in *Combinatorial and Additive Number Theory*, Springer (2014), pp. 147–157.
