# An exact facet generating function for diameter-two truncated path metrics

## Finding

Let \(M_n=\{1,\ldots,n\}\), with integer \(n\ge2\), have the *capped-path metric*
\[
d(i,j)=\min\{|i-j|,2\}.
\]
Write \(F_n\) for the number of facets of the unit ball of the real Lipschitz-free space \(\mathcal F(M_n)\). Then
\[
\boxed{\sum_{n\ge2}F_n z^n=\frac{2z^2}{1-z}+\frac{2z^3(1+z)^3}{(1-z-2z^2-2z^3)(1-z-z^2-z^3)}.}
\]
The values for \(n=2,\ldots,10\) are
\[
2,\ 4,\ 12,\ 32,\ 84,\ 216,\ 536,\ 1304,\ 3124.
\]
In particular, for some explicit \(C>0\),
\[
\boxed{F_n\sim C\lambda^n,\quad \lambda=2.269530842081\ldots,\quad C=1.05688745\ldots,}
\]
where \(\lambda\) is the unique positive root of \(\lambda^3-\lambda^2-2\lambda-2=0\). The growth base is strictly greater than two, the corresponding base for untruncated path metrics.

## Assumptions and scope

All spaces, functionals, and convex polytopes are real. Fix the basepoint \(1\). The dual unit ball is the full-dimensional Lipschitz polytope
\[
P_n=\bigl\{f\in\mathbb R^n:f(1)=0,\ |f(i)-f(j)|\le\min\{|i-j|,2\}\text{ for all }i,j\bigr\}.
\]
Its vertices are in bijection with facets of the (polar) Lipschitz-free unit ball, so it suffices to count its vertices. Two potentials differing by a constant are identified; for classification it is convenient to subtract their minimum instead of fixing the basepoint. All distances belong to \(\{0,1,2\}\), and the metric has diameter two. For \(n\ge4\), it is not a tree metric: on points \(1,2,3,4\), the three four-point sums are \(d(1,2)+d(3,4)=2\), \(d(1,3)+d(2,4)=4\), and \(d(1,4)+d(2,3)=3\), whereas a tree metric requires the two largest to coincide.

## Proof

**1. Tight-edge criterion and integrality.** For \(f\in P_n\), join distinct indices \(i,j\) in a graph \(T_f\) exactly when \(|f(i)-f(j)|=d(i,j)\). The active normals of these inequalities are the oriented edge-incidence vectors. Their rank modulo the constant direction is \(n-c(T_f)\), where \(c\) denotes the number of connected components. Consequently \(f\) is a vertex of \(P_n\) if and only if \(T_f\) is connected: connectedness gives rank \(n-1\) and uniqueness after basepoint normalization, whereas disconnectedness permits small nontrivial componentwise shifts preserving every slack inequality. This criterion is standard (Gordon–Petrov and related treatments), not claimed as new.

Every saturated edge has integer potential difference \(1\) or \(2\). Thus, if \(T_f\) is connected, all potential values differ by integers. Subtracting the minimum yields a string \(w=(w_1,\ldots,w_n)\) with letters in \(\{0,1,2\}\). A vertex cannot be constant, so its range is exactly one or two. Distinct normalized strings correspond bijectively to distinct vertices of \(P_n\).

**2. Range-one strings.** If \(\max w-\min w=1\), the letters are zero and one. All pairs at separation at least two have distance two and cannot be saturated. Therefore \(T_f\) is connected precisely when every consecutive pair has opposite values. Exactly two strings satisfy this: the two alternating binary strings.

**3. Range-two strings.** Now both zero and two occur. Feasibility prohibits consecutive zero and two, since consecutive indices have distance one. Every zero and every two are therefore separated by at least two positions, so the edges between the entire zero class and the entire two class are saturated, forming a connected complete bipartite core. A vertex bearing one can have a saturated edge only to a zero or a two at an *adjacent* index: its value differs from either extreme by one, while pairs at separation at least two have distance two. It follows that \(T_f\) is connected if and only if *every occurrence of one is adjacent in the index order to at least one occurrence of zero or two*. These conditions are sufficient for feasibility as well: adjacent differences are at most one and all other differences are at most two. Equivalently, each interior run of ones has length at most two, and each leading or trailing run of ones has length at most one.

**4. Enumerating admissible strings.** Let \(R(z)=z/(1-z)\), marking a nonempty monochromatic block of zeros or twos, and \(S(z)=z+z^2\), marking an internal run of one or two symbols one. Such a string consists of an optional leading one, a nonempty sequence of colored blocks separated by internal runs of ones, and an optional trailing one. The generating function for all these strings (allowing either or both extreme colors) is
\[
(1+z)^2\frac{2R(z)}{1-2R(z)S(z)}.
\]
Strings using only zero blocks, and likewise strings using only two blocks, each contribute \((1+z)^2R(z)/(1-R(z)S(z))\). Removing these two disjoint one-color classes enforces the presence of both extrema, yielding
\[
\begin{aligned}
H(z)&=(1+z)^2\left(\frac{2R(z)}{1-2R(z)S(z)}-\frac{2R(z)}{1-R(z)S(z)}\right)\\
&=\frac{2z^3(1+z)^3}{(1-z-2z^2-2z^3)(1-z-z^2-z^3)}.
\end{aligned}
\]
This is precisely the generating function for range-two extreme potentials. There are two range-one extremes at every length \(n\ge2\), so adding \(2z^2/(1-z)\) proves the displayed facet formula by polarity.

**5. Exact exponential asymptotic.** Put \(A(z)=1-z-2z^2-2z^3\) and \(B(z)=1-z-z^2-z^3\). The smallest-modulus zero of \(A\) is its unique positive zero \(\rho\); it is simple because \(A'(\rho)<0\). Its uniqueness on its circle follows from the equality case of the triangle inequality in \(1=\rho+2\rho^2+2\rho^3\) and the presence of consecutive exponents. Furthermore \(B(\rho)=\rho^2+\rho^3>0\), while the positive zero of \(B\) occurs strictly beyond \(\rho\). The pole at \(\rho\) is therefore the unique dominant pole of the rational function, and ordinary coefficient extraction gives
\[
F_n\sim C\rho^{-n},\qquad
C=\frac{-2\rho^3(1+\rho)^3}{\rho A'(\rho)B(\rho)}>0.
\]
The reciprocal \(\lambda=1/\rho\) satisfies \(\lambda^3-\lambda^2-2\lambda-2=0\), and lies strictly between two and three.

## Verification

The standalone standard-library script `verify_capped_path.py` checks every normalized ternary string for lengths \(n=2,\ldots,10\) against the original metric inequalities and connectivity of the *full* tight-edge graph. It separately recognizes the claimed binary and ternary string classes, and computes the coefficients from an independent integer-polynomial recurrence for the rational generating function. All three approaches agree: 86,525 normalized candidates were examined, including 5,314 predicted and directly verified vertices, reproducing \(2,4,12,32,84,216,536,1304,3124\). Execute with `python verify_capped_path.py`.

As a separate numerical check, halfspace-intersection vertex enumeration with SciPy/Qhull for \(n=3,4,5,6\) returned \(4,12,32,84\) vertices. These finite calculations test implementation and small instances only; they do not establish the all-length theorem, which follows from the analytic classification and generating functions above.

## Relationship to prior work

Gordon and Petrov characterize admissible saturated-edge graphs and determine the face numbers of *generic* finite metrics; their results provide the general rank viewpoint. The capped-path metric has many tight triangle equalities and is not generic, so the generic face-number formula does not specialize to this case. Delucchi and Hoessly enumerate face numbers for *tree-like* metrics; the explicit four-point obstruction above excludes the capped path for all \(n\ge4\). Alexander, Fradelizi, García-Lirola and Zvavitch investigate finite-dimensional Lipschitz-free polytope geometry but do not supply the present word classification or rational facet-count generating function in the examined portions. Bredies, Chirinos Rodriguez and Naldi characterize extreme Lipschitz maps using saturated-constraint connectedness in broader settings; the rank criterion is prior knowledge, while the special capped-path classification, count, and asymptotic are the new conclusions.

Related published exact facet formulas exist for equilateral metrics with independently shortened *disjoint* pairs and for complete multipartite interpolations. Our strict short edges are all consecutive edges of a path and overlap at interior vertices; neither earlier restricted formula applies by specialization. Searches for capped-path/truncated-line metric dual extreme counts and comparisons with accessible related results found no equivalent formula. Absence of indexed matches does not rule out unindexed or differently formulated prior work.

## Limitations

Only real scalars, the integer cap two, and finite path point sets are covered. No classification is claimed for arbitrary caps, weighted paths, higher face numbers, or complex Lipschitz spaces. The first two small lengths and standard connected-tight-graph principle are known special or general facts; the new substantive result is the all-length capped-path classification and exact count. The originality review is necessarily limited by accessible and indexed literature, and no independent scientific audit has been carried out.

## References

- J. Gordon and F. Petrov, *Combinatorics of the Lipschitz Polytope*, arXiv:1608.06848, first public 2016-08-24, https://arxiv.org/abs/1608.06848.
- E. Delucchi and L. Hoessly, *Fundamental Polytopes of Metric Trees via Parallel Connections of Matroids*, arXiv:1612.05534, first public 2016-12-16, https://arxiv.org/abs/1612.05534.
- M. Alexander, M. Fradelizi, L. García-Lirola and A. Zvavitch, *Geometry and Volume Product of Finite Dimensional Lipschitz-Free Spaces*, arXiv:1911.10642, first public 2019-11-24, https://arxiv.org/abs/1911.10642.
- K. Bredies, J. Chirinos Rodriguez and E. Naldi, *On Extreme Points and Representer Theorems for the Lipschitz Unit Ball on Finite Metric Spaces*, arXiv:2304.14039, first public 2023-04-27, https://arxiv.org/abs/2304.14039.
