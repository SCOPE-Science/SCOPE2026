# Threshold functions determine the exact algebraic degree of parallelotope cutoff volumes

## Finding

For every integer \(d\ge 1\) and every full-dimensional parallelotope \(K\subset\mathbb R^d\), the smallest possible degree in the volume variable of a nonzero *global polynomial cutoff-volume relation* is exactly
\[
\boxed{\delta(K)=T_d-2},
\]
where \(T_d\) is the number of affine Boolean linear threshold functions on the labeled vertices of a \(d\)-cube, including the two constant functions (OEIS A000609). In particular, the first five values of this sharp algebraic degree are \(2,12,102,1880,94570\). The threshold counts are established combinatorial data, **not** claimed to have been newly enumerated.

More concretely, let \(Q_d=[0,1]^d\), let \(\mathcal T_d^\circ\) be the set of nonempty proper vertex subsets strictly separable by an affine hyperplane, and define for each such subset
\[
N_J(\eta,s)=\sum_{v\in J}(-1)^{|v|}(s-\langle\eta,v\rangle)^d,
\qquad |v|=\sum_{i=1}^{d}v_i.
\]
An explicit degree-minimizing polynomial for \(Q_d\) is
\[
\boxed{P_d(\eta,s,w)=\prod_{J\in\mathcal T_d^\circ}
\left(d!\Bigl(\prod_{i=1}^{d}\eta_i\Bigr)w-N_J(\eta,s)\right).}
\]
It vanishes upon substituting the actual clipped volume into \(w\) for **every** hyperplane intersecting the interior, including exceptional normals with zero coordinates. No nonzero relation of smaller degree in \(w\) exists.

## Assumptions and scope

Write a general parallelotope as \(K=b+A[0,1]^d\), with \(A\) a real invertible \(d\times d\) matrix. For \(\eta\in\mathbb R^d\setminus\{0\}\) and \(s\in\mathbb R\), set
\[
V_K(\eta,s)=\operatorname{vol}_d\{x\in K:\langle\eta,x\rangle\le s\}.
\]
Only **interior cuts**, meaning
\[
\min_{x\in K}\langle\eta,x\rangle<s<\max_{x\in K}\langle\eta,x\rangle,
\]
are required by the relation. Let \(\delta(K)\) be the minimum \(\deg_w P\) over all nonzero polynomials \(P\in\mathbb R[\eta_1,\ldots,\eta_d,s,w]\) satisfying \(P(\eta,s,V_K(\eta,s))=0\) on this entire domain. This is **not** an irreducible minimal polynomial over \(\mathbb R(\eta,s)\): the actual cutoff-volume function is piecewise rational, with many rational branches.

An affine Boolean threshold function is a labeling of \(\{0,1\}^d\) by two values for which some affine hyperplane strictly separates the positive- and negative-labeled vertices. The two constant labelings are allowed in \(T_d\), but cannot represent interior cuts; hence \(|\mathcal T_d^\circ|=T_d-2\).

## Proof

**Step 1: exact branch formula.** Suppose initially that \(\eta_i\ne0\) for every coordinate. The classical clipped-cube formula is
\[
V_{Q_d}(\eta,s)=\frac{1}{d!\prod_{i=1}^{d}\eta_i}
\sum_{v\in\{0,1\}^d}(-1)^{|v|}(s-\langle\eta,v\rangle)_+^d,
\qquad a_+=\max\{a,0\}.
\tag{1}
\]
The formula applies to either sign of every \(\eta_i\). For completeness, it follows inductively by integrating the cumulative volume in the last coordinate:
\[
V_{Q_d}(\eta,s)=\int_0^1 V_{Q_{d-1}}(\eta',s-\eta_d t)\,dt
=\frac1{\eta_d}\int_{s-\eta_d}^{s}V_{Q_{d-1}}(\eta',u)\,du.
\]
The final integral is an *oriented* integral if \(\eta_d<0\), so the displayed identity still holds. The one-dimensional starting case is \(((s)_+-(s-\eta_1)_+)/\eta_1\); each integration increases the truncated-power exponent and introduces its factorial factor. This proves (1) for every dimension by induction.

**Step 2: branches indexed by all nontrivial threshold functions.** For each \(J\in\mathcal T_d^\circ\), the parameter set
\[
\Omega_J=\{(\eta,s):\langle\eta,v\rangle<s\ \text{for }v\in J,
\quad\langle\eta,v\rangle>s\ \text{for }v\notin J,\quad\prod_i\eta_i\ne0\}
\]
is nonempty and open. A strict separating witness can be perturbed to make every coordinate of \(\eta\) nonzero without changing the finite labeling. On this chamber (1) becomes the single rational function
\[
V_{Q_d}(\eta,s)=F_J(\eta,s):=\frac{N_J(\eta,s)}{d!\prod_i\eta_i}.
\tag{2}
\]
Every member of \(\mathcal T_d^\circ\) corresponds to a genuine interior cut because both vertex classes are nonempty.

**Step 3: distinct labels give distinct rational functions.** Expand \(N_J\) into homogeneous monomials in \((\eta,s)\). For any \(S\subseteq\{1,\ldots,d\}\), the coefficient of the **squarefree monomial**
\(s^{d-|S|}\prod_{i\in S}\eta_i\) is
\[
(-1)^{|S|}\frac{d!}{(d-|S|)!}
\sum_{v\in J}(-1)^{|v|}\prod_{i\in S}v_i.
\tag{3}
\]
The sum on the right equals \(\sum_{U\supseteq S}(-1)^{|U|}{\bf1}_{U\in J}\), after identifying a cube vertex with the support of its coordinates. These \(2^d\) upper-set sums determine all \(2^d\) signed membership indicators through elementary Boolean-lattice Möbius inversion. Thus \(N_J=N_{J'}\) implies \(J=J'\); in particular the rational functions in (2) are pairwise distinct in \(\mathbb R(\eta,s)\). This injectivity holds for **all** vertex subsets, not just threshold subsets.

**Step 4: irreducible-degree-free lower bound.** Let \(Q(\eta,s,w)\) be any nonzero polynomial satisfying the full interior-cut relation. For each \(J\), substituting (2) gives \(Q(\eta,s,F_J(\eta,s))=0\) on the open set \(\Omega_J\). Clearing powers of \(\prod_i\eta_i\) yields a polynomial in \((\eta,s)\) vanishing on a nonempty open set; it therefore vanishes identically. Hence \(F_J\) is a root of \(Q\) regarded as a polynomial over the field \(\mathbb R(\eta,s)\). The \(T_d-2\) distinct roots from Step 3 force
\[
\deg_w Q\ge T_d-2.
\tag{4}
\]
No numerical enumeration is needed for this all-dimensional argument.

**Step 5: matching upper bound and degenerate normals.** By Step 2, the explicit polynomial \(P_d\) in the Finding vanishes on every generic interior-cut chamber. It has exactly \(T_d-2\) linear factors in \(w\), each with the same nonzero polynomial leading coefficient; thus \(\deg_w P_d=T_d-2\). Since both \(V_{Q_d}\) and \(P_d\) are continuous in all their real arguments, approximate any interior cut with a normal having a zero coordinate by generic interior cuts. The relation persists in the limit. Therefore (4) is sharp on the required entire domain.

**Step 6: affine invariance.** For \(K=b+A Q_d\), the change of variables gives
\[
V_K(\eta,s)=|\det A|\,V_{Q_d}(A^{\mathsf T}\eta,s-\langle\eta,b\rangle).
\]
The transformation of \((\eta,s,w)\) determined by \(A,b,|\det A|\) is an invertible linear change of variables preserving degree in \(w\). Existence and minimality therefore transfer from \(Q_d\) to every full-dimensional parallelotope. This completes the proof.

## Verification

The included standalone Python 3 program `verify.py` uses only standard-library exact rational arithmetic and integer operations. Executed directly, it returned:

`CUBE_DEGREE_CHECK_OK: 72172 exact finite checks; witness counts 2,12,102,1880; signed 2D clipping verified`

It compares strict integer-weight threshold witnesses in dimensions one through four against independently established published counts, tests the coefficient-signature injectivity across **all** Boolean assignments in those dimensions, and compares the signed truncated-power formula with exact rational polygon clipping of the square. The finite weight searches do **not** prove enumeration completeness; the table values are externally established. The general theorem follows from Steps 1–6, not from numerical tests.

## Relationship to prior work

Shan (arXiv:2610.19660, first public October 14, 2026) proves a smooth-body algebraic-integrability classification and observes that every full-dimensional polytope is algebraically integrable. That observation supplies existence, not the smallest degree in the *volume variable* of an equation valid for all cutting hyperplanes.

Cho–Kim (arXiv:1512.07768) and Lasserre (arXiv:1412.4617), following older truncated-power formulas, supply known exact hypercube and simplex cutoff-volume formulas. Formula (1) is explicitly prior machinery, not itself a new result. Brandenburg–Meroni (arXiv:2510.09265) analyze the threshold arrangement and its relation to combinatorial types of cube *sections*, and Brandenburg–De Loera–Luo–Meroni (arXiv:2603.25643) give piecewise rational *section/slab* moments. Neither inspected account identifies the minimal global polynomial degree for the **cumulative cutoff volume**, nor proves the distinct-branch lower bound (3)–(4). The standard counts \(T_d\) are OEIS A000609. The proposed contribution is the sharp all-dimensional identity \(\delta(K)=T_d-2\), including the Möbius-inversion argument establishing that each threshold chamber forces a genuinely distinct rational root.

## Limitations

This is a sharp global-degree statement for **full-dimensional parallelotopes only**. It does not classify all polytopes, determine coefficient or total degree of the product relation, or assert that the displayed reducible product is an irreducible algebraic minimal polynomial. For each *fixed* normal, far fewer pieces occur. The listed low-dimensional threshold counts are established external combinatorial data; the verifier's bounded search is not a proof of their completeness. Earlier work on piecewise-rational algebraic relations could contain an equivalent interpretation, so historical priority remains provisional; no independent review has been performed.

## References

1. Junjie Shan, *Algebraically Integrable Smooth Convex Bodies*, arXiv:2610.19660 (first publicly available 2026-10-14), Introduction and Definition 1.1.
2. Yunhi Cho and Seonhwa Kim, *Volume of Hypercubes Clipped by Hyperplanes and Combinatorial Identities*, arXiv:1512.07768 (2015), Introduction and Theorem 1.
3. Jean B. Lasserre, *Volume of slices and sections of the simplex in closed form*, arXiv:1412.4617 (2014), Section 2.3.
4. Marie-Charlotte Brandenburg and Chiara Meroni, *Combinatorics of slices of cubes*, arXiv:2510.09265 (2025), Section 1, “Threshold functions” and “Volumes.”
5. Marie-Charlotte Brandenburg, Jesús A. De Loera, Yu Luo, and Chiara Meroni, *Critical moments of slices and slabs of the cube (and other polyhedral norms)*, arXiv:2603.25643 (2026), Introduction and Theorem 1.
6. OEIS Foundation, *A000609: Number of threshold functions of n or fewer variables*, https://oeis.org/A000609 (counts and references).
