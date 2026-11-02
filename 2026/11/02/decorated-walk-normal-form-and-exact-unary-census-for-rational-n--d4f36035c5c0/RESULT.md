# Decorated-walk normal form and exact unary census for rational non-expansive fuzzy terms

## Finding

Fix any integer \(d\geq1\) and let \(G_d=\{0,1/d,\ldots,1\}\). For the one-variable, modal-free non-expansive fuzzy propositional language with truth constants and shift amounts in \(G_d\), the distinct real-valued term functions have an exact, finite decorated-walk normal form.

Write \(\mathcal T_d\) for the set of all functions \(f:[0,1]\to[0,1]\) defined by finite terms in this language, identifying terms if they agree on every real input. Each function is completely and uniquely determined by its samples at the half-grid \(\{j/(2d):0\leq j\leq2d\}\). For every \(k=0,\ldots,d-1\), put \(a=df(k/d)\) and \(b=df((k+1)/d)\). Both are integers from \(0\) through \(d\). Necessarily \(|a-b|\leq1\). The graph on this full-grid cell is:

- the unique increasing line when \(b=a+1\);
- the unique decreasing line when \(b=a-1\);
- precisely one of the constant line, the upward midpoint tent (allowed when \(a<d\)), or the downward midpoint tent (allowed when \(a>0\)), when \(b=a\).

Every sequence of these allowed cell types, with matching endpoints, is the graph of a term function in \(\mathcal T_d\). This is a genuine normal form: two different decorated paths define different real functions.

Define the symmetric tridiagonal \((d+1)\)-by-\((d+1)\) integer matrix \(A_d\), indexed by \(0,\ldots,d\), by
\[
(A_d)_{ij}=\begin{cases}
1,&|i-j|=1,\\
2,&i=j\in\{0,d\},\\
3,&i=j\in\{1,\ldots,d-1\},\\
0,&\text{otherwise}.
\end{cases}
\]
For \(d=1\), both diagonal entries are \(2\). With \(\mathbf 1\) the all-ones column vector, the **exact number of distinct unary truth functions** is
\[
\boxed{|\mathcal T_d|=\mathbf1^{\mathsf T}A_d^d\mathbf1.}
\]
In particular, for \(d=1,\ldots,8\), the numbers are
\[
6,\ 43,\ 296,\ 1925,\ 11970,\ 71983,\ 422084,\ 2427113.
\]
The cardinalities also satisfy the sharp leading-order growth law
\[
\boxed{|\mathcal T_d|=5^d\bigl(d+O(\sqrt d)\bigr)\sim d\,5^d}\qquad(d\to\infty).
\]
The parameter \(d\) controls the *permitted syntax*, not a restriction of valuations to a finite truth set: the functions are distinguished on the entire real unit interval.

## Assumptions and scope

The input alphabet consists of one propositional variable \(x\), all constants \(c\in G_d\), binary \(\min\) and \(\max\), unary negation \(N(u)=1-u\), and unary clipped shifts
\[
P_c(u)=\min(1,u+c),\qquad M_c(u)=\max(0,u-c),\qquad c\in G_d.
\]
All operations act pointwise on \([0,1]\). No modalities, discontinuities, unrestricted binary truncated addition, or arbitrary real truth constants are allowed. Nested shifts and arbitrary finite min-max combinations are allowed. Equality of functions means extensional equality for all \(x\in[0,1]\), not equality only on the basic grid.

The normal-form graph is a weighted nearest-neighbour walk on the vertex set \(\{0,1,\ldots,d\}\) of length exactly \(d\). A step from \(a\) to \(a\pm1\) has weight one; a step staying at an interior vertex has weight three (flat, up-tent, down-tent); a step staying at an endpoint has weight two (flat and one inward tent). These weights are decorations, not probabilistic transition probabilities.

## Proof

**Step 1: affine-component invariant.** Every term is a continuous, piecewise-affine function whose nondegenerate affine components are of the forms
\[
\text{constant }j/d,\quad x+j/d,\quad -x+j/d,\qquad j\in\mathbb Z.
\]
This follows by structural induction. It holds for the variable and each truth constant. Complement replaces a slope by its negative and changes the integral-grid intercept; clipped shifts replace affine components by their translates or by the endpoint constants; and min/max of piecewise-affine functions selects one of the existing affine pieces after finitely many crossings. The stated family is therefore closed under all the allowed operations. On any nonempty open interval where a component is constant and realized by a term valued in \([0,1]\), its constant value belongs to \(G_d\).

**Step 2: where bends can occur.** Two nonparallel lines from this component family meet only at grid or half-grid abscissae: slopes differing by one cross at integral multiples of \(1/d\), and slopes differing by two cross at integral multiples of \(1/(2d)\). Parallel distinct lines never meet. Thus the function is affine on each open half-grid cell, and continuous at its endpoints. Its values at full-grid points are multiples of \(1/d\): any affine component evaluated there has this property. Every half-grid segment has slope in \(\{-1,0,1\}\), so its half-grid endpoint values differ by at most \(1/(2d)\). Two consecutive such increments sum to \((b-a)/d\), hence \(b-a\in\{-1,0,1\}\). If this difference is \(\pm1\), both increments are forced to have that sign. If it is zero, the two increments are necessarily \((0,0)\), \((1,-1)\), or \((-1,1)\) in the integer half-grid vertical scale. The tent options are forbidden only when they would leave \([0,1]\) at the midpoint. This proves necessity and uniqueness of the decorated-walk encoding.

**Step 3: sufficiency via lattice-polynomial representation.** Conversely, join the segments prescribed by any allowed decorated walk. The resulting function \(f\) is continuous, takes values in \([0,1]\), and has affine components among the lines listed in Step 1. Ovchinnikov's max-min representation theorem (2002, Theorem 2.1) applies to the convex domain \([0,1]\). It expresses every continuous piecewise-affine function on that interval as a finite max-min polynomial in its own affine components. To realize that polynomial in the present language, replace each affine component \(\ell\) by its clipping \(\operatorname{clip}(\ell)=\max(0,\min(1,\ell))\). Since clipping is monotone and distributes over finite min and max, the polynomial then evaluates to \(\operatorname{clip}(f)=f\). Each clipped positive-slope component is a repeated rational shift of \(x\); each clipped negative-slope component is a repeated rational shift of \(1-x\); each constant component is already an allowed truth constant. (For integral-grid intercepts whose absolute values exceed one, iterated shifts still give the appropriate constant endpoint.) Hence \(f\) is definable by a term. The continuous pieces fit exactly and no unproved interpolation or infinite approximation is involved.

**Step 4: exact enumeration.** By Steps 2 and 3, a term function is the same object as a length-\(d\) decorated walk with arbitrary initial and final vertices in \(\{0,\ldots,d\}\). The one-step transfer matrix is exactly \(A_d\). Summing all entries of its \(d\)-th power proves the claimed formula and the displayed finite values.

**Step 5: asymptotic.** Every row of \(A_d\) has total weight at most five, so
\[
|\mathcal T_d|\le(d+1)5^d.
\]
For the reverse bound, start an independent-increment walk at each interior height \(i\) with increments \(+1,0,-1\) of respective probabilities \(1/5,3/5,1/5\). Give its zero increments three distinguishable labels. Every length-\(d\) labelled path that avoids both boundary vertices throughout is an allowed decorated walk. Its martingale has variance \(2d/5\) at time \(d\). The maximal inequality gives, for \(r_i=\min(i,d-i)\ge1\),
\[
\Pr_i(\text{visit a boundary by step }d)\le
\min\!\left\{1,\frac{2d}{5r_i^2}\right\}.
\]
Summing over starting heights yields
\[
|\mathcal T_d|\ge5^d\left[(d-1)-2\sum_{r=1}^{\lfloor d/2\rfloor}\min\!\left\{1,\frac{2d}{5r^2}\right\}\right]
=5^d\bigl(d-O(\sqrt d)\bigr).
\]
The last estimate follows by separating \(r\le\sqrt d\) and the convergent tail \(\sum_{r>\sqrt d}r^{-2}=O(d^{-1/2})\). Together with the upper bound this proves \(|\mathcal T_d|=5^d(d+O(\sqrt d))\), with an absolute implicit constant.

## Verification

The accompanying `checker.py` uses only Python's standard library and computes independent fixed points under the **full stated syntax**, not just the clipped affine generators. It represents a term function exactly by its integer-scaled values \(2d\,f(j/(2d))\) on all \(2d+1\) half-grid vertices. For each \(d=1,2,3\), it closes the initial variable and rational constants under negation, every allowed clipped shift, min, and max. Independently, it enumerates every allowed decorated walk, and independently computes the transfer-matrix total. These three constructions agree exactly:
\[
\begin{array}{c|rrr}d&1&2&3\\\hline |\mathcal T_d|&6&43&296\end{array}.
\]
The same checker evaluates the matrix formula for \(d\le8\), giving the eight values stated in the Finding section. Run `python3 checker.py` and require the final line `ALL_CHECKS_OK`. Finite closure checks corroborate but do not replace the all-\(d\) proof.

## Relationship to prior work

Gebhart, Schröder, and Wild introduced and studied non-expansive fuzzy logics with truth constants and constant shifts (2025), including satisfiability complexity. Their 2026 paper establishes uniform interpolation for the non-expansive fuzzy modal language and discusses propositional normal forms and elimination. Those results motivate this concrete fixed-denominator, one-variable term-expressivity question, but the inspected full texts do not state the decorated-walk classification, transfer-matrix cardinality, or \(d5^d\) asymptotic.

Ovchinnikov (2002) proved the general max-min representation for arbitrary continuous piecewise-affine functions on convex domains. That theorem is explicitly used for the representability direction; it does **not**, by itself, count the rationally restricted unary functions. The present restricted-component invariant, exact decorated-walk parametrization, and asymptotic census supply the additional quantitative content.

Related finite-grid variable-elimination results concern where extrema are attained, not how many distinct unary term functions the language defines. Equality of themes or a shared grid parameter does not imply the cardinality theorem. An earlier representation or enumeration in a different finite-automata, lattice-function, or algebraic-logic vocabulary is a residual historical-priority risk.

## Limitations

The result is restricted to one real-valued variable and a **fixed denominator** of rational truth constants and shifts. It does not classify multivariable functions, modal term semantics, unrestricted rational constants across all denominators, or full binary Łukasiewicz operations. The asymptotic counts semantic functions, not syntax trees or minimum formula lengths. No independent audit has been performed; older equivalent enumerations may exist under different vocabulary.

## References

1. S. Gebhart, L. Schröder, P. Wild, *Non-Expansive Fuzzy Modal Logic Has Uniform Interpolation*, arXiv:2610.32335v1, publicly posted 2026-10-23. https://arxiv.org/html/2610.32335v1
2. S. Gebhart, L. Schröder, P. Wild, *Non-expansive Fuzzy ALC*, arXiv:2505.09416; IJCAI 2025, pp. 4509–4517. https://www.ijcai.org/proceedings/2025/0502.pdf
3. S. Ovchinnikov, *Max-Min Representation of Piecewise Linear Functions*, Beiträge zur Algebra und Geometrie 43 (2002), 297–302, Theorem 2.1; arXiv:math/0009026. https://arxiv.org/abs/math/0009026
