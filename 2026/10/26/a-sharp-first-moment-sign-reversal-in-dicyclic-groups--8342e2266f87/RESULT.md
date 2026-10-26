# A sharp first-moment sign reversal in dicyclic groups

## Finding
Let \(G_n=\operatorname{Dic}_n=\langle a,b\mid a^{2n}=1,\ b^2=a^n,\ bab^{-1}=a^{-1}\rangle\), the dicyclic group of order \(4n\), for every integer \(n\ge2\). For every \(A\subseteq G_n\), put \(d(A)=|AA|-|AA^{-1}|\), where \(AA^{-1}=\{xy^{-1}:x,y\in A\}\). Its unnormalized first moment is \(M(n)=\sum_{A\subseteq G_n}d(A)\).

**The exact sign threshold is \(n=30\):**
\[
M(n)<0\quad(2\le n\le29),\qquad M(n)>0\quad(n\ge30).
\]
In particular, the first positive first moment in this family occurs at group order \(120\), and the boundary values are
\[
M(29)=-203011530049362987071455440,\qquad
M(30)=397569666293094423242677920.
\]
This is a statement about the *mean* of \(d(A)\), not about whether more subsets have positive or negative \(d(A)\).

## Assumptions and scope
For integers \(j\ge1\), let \(I_j\) count independent subsets of a cycle of length \(j\), with the loop convention \(I_1=1\), \(I_2=3\), and \(I_j=I_{j-1}+I_{j-2}\) for \(j\ge4\), where \(I_3=4\). Thus \(I_j\) for \(j\ge2\) are Lucas numbers. Write \(m=2n\), \(c_t=\gcd(m,t)\), \(h_t=\gcd(m,n-t)\), \(\epsilon_t=1\) for even \(t\) and \(0\) for odd \(t\). Use \(\gcd(m,0)=m\).

The following exact formula holds for every integer \(n\ge2\):
\[
\boxed{M(n)=-4n7^{n-1}+\sum_{t=0}^{2n-1}
\left(I_{2n/c_t}^{2c_t}-3^{n-\epsilon_t}I_{2n/h_t}^{h_t}\right).}
\]
All quantities are integers; no approximation is used in the finite verification.

## Proof
**1. Missing-element identity.** For \(g\in G_n\), let \(F_P(g)\) be the number of subsets \(A\) with \(g\notin AA\), and \(F_Q(g)\) the number with \(g\notin AA^{-1}\). Interchanging two finite sums gives \(M(n)=\sum_{g\in G_n}(F_Q(g)-F_P(g))\). The quotient constraint \(xy^{-1}=g\) is equivalent to \(x=gy\). Hence \(F_Q(g)=I_{\operatorname{ord}(g)}^{4n/\operatorname{ord}(g)}\) by the disjoint cycles of the left-multiplication permutation. For products, \(xy=g\) is equivalent to \(y=x^{-1}g\); thus \(F_P(g)\) is the number of independent sets in the undirected cycle graph of the permutation \(\phi_g(x)=x^{-1}g\). A fixed point represents a forbidden loop and contributes \(I_1=1\).

**2. Rotations.** Let \(g=a^t\), with \(0\le t<2n\). On the \(2n\) rotation elements, \(\phi_g(a^i)=a^{t-i}\), an involution with exactly two fixed points if \(t\) is even and none otherwise. This contributes \(3^{n-\epsilon_t}\). On the other coset, \(\phi_g(a^ib)=a^{i+n-t}b\) cyclically shifts exponents by \(n-t\). It has \(h_t\) cycles each of length \(2n/h_t\). Thus \(F_P(a^t)=3^{n-\epsilon_t}I_{2n/h_t}^{h_t}\). Since \(a^t\) has order \(2n/c_t\), \(F_Q(a^t)=I_{2n/c_t}^{2c_t}\).

**3. Nonrotation coset.** For \(g=a^tb\), the map \(\phi_g\) takes \(a^i\) to \(a^{t-i}b\) and \(a^jb\) to \(a^{j-t}\). Its square acts by \(i\mapsto-i\) on rotations. There are two cycles of length two and \(n-1\) cycles of length four, so \(F_P(a^tb)=3^2 7^{n-1}\). All these \(2n\) elements have order four, giving \(F_Q(a^tb)=7^n\). Consequently their total contribution to \(M(n)\) is \(-4n7^{n-1}\). Combining these cases proves the displayed exact formula.

**4. Infinite-range positivity.** The terms \(t=0,n\) together contribute
\[
1+\frac23 9^n-3^{n-\mathbf1_{2\mid n}}\ \ge\ 1+\frac23 9^n-3^n.
\]
For any remaining \(t\), the rotation-coset cycle length \(L=2n/h_t\) is at least three. Since \(I_3=4<(5/3)^3\), \(I_4=7<(5/3)^4\), and \((5/3)^2>(5/3)+1\), induction through the Lucas recurrence proves \(I_L\le(5/3)^L\) for every \(L\ge3\). Hence \(F_P(a^t)\le 3^n(5/3)^{2n}=(25/3)^n\). Dropping the nonnegative \(F_Q(a^t)\) terms gives the rigorous lower bound
\[
\frac{M(n)}{9^n}\ge\frac23+9^{-n}-3^{-n}-(2n-2)(25/27)^n
-\frac{4n}{7}(7/9)^n.
\]
At \(n=80\), even the right side with \(9^{-n}\) deleted is **strictly positive by exact rational arithmetic** (checked in `check_dicyclic_moment.py`). The three negative quantities \(3^{-n}\), \((2n-2)(25/27)^n\), and \((4n/7)(7/9)^n\) decrease strictly for all \(n\ge80\), so \(M(n)>0\) for every \(n\ge80\).

**5. Exact finite threshold.** The standalone integer-arithmetic recurrence in `check_dicyclic_moment.py` computes the finite sum above for each \(2\le n\le79\). It checks \(M(n)<0\) for \(2\le n\le29\) and \(M(n)>0\) for \(30\le n\le79\). Together with Step 4, this proves the universal assertion.

## Verification
Run `python3 check_dicyclic_moment.py` to check every finite sign, the two boundary integers, the six smallest moments, and the exact positive rational lower bound at \(n=80\). As an independent finite cross-check, compile `check_small_dicyclic.c` using `cc -O2 -std=c11 check_small_dicyclic.c -o check_small_dicyclic` and run `./check_small_dicyclic`; it enumerates every subset of \(G_n\) for \(2\le n\le6\) directly from a multiplication table, checks the group law and inverses, and reproduces first moments \(-32,-156,-5376,-47280,-779184\). The full infinite-range proof uses the explicit bound of Step 4, not extrapolation from enumeration.

## Relationship to prior work
Amit, Chen, Housholder, Im, Khan, Miller, Palomares and Pradhan (2026), especially §§3, 7 and 8, express first moments in terms of forbiddance graphs and general character-theoretic cycle counts; §8 explicitly identifies dicyclic groups as outside the immediate reach of their asymptotic dominance conditions and suggests detailed moment analysis. Their general formula does **not state or determine the sharp \(n=30\) sign threshold** without specializing and analyzing its terms. Mandal and Neetu (2026) tabulate subset counts by cardinality for dicyclic groups of orders at most 20 and prove small-cardinality formulas; those finite tables do not cover order 120 or establish an infinite sign transition. The proof here specializes the product and quotient cycle graphs directly, supplies a closed arithmetic formula and proves the sharp sign threshold by a finite exact sweep combined with a uniform infinite tail inequality.

## Limitations
A positive first moment need not mean that product-dominant subsets are more numerous than quotient-dominant ones. This result does not classify dicyclic groups by that stronger criterion, nor does it assert a sharp first-moment *ratio*. The finite sign verification uses ordinary exact-arithmetic code rather than a separately formalized proof assistant. Prior implicit coverage in unindexed sources cannot be ruled out.

## References
1. Y. Amit et al., *Product and Quotient Set Dominance in Finite Groups*, arXiv:2610.12912v1 (2026-10-09), https://arxiv.org/html/2610.12912v1, §§3,7,8.
2. S. Mandal and Neetu, *Exact and Asymptotic Counts of MSTD, MDTS, and Balanced Sets in Dicyclic Groups*, arXiv:2602.09073v1 (2026-02-09), https://arxiv.org/pdf/2602.09073, pp. 1–4, 18–19.
