# An exact branch-collision determinant for one-gauge linear drainage trees

## Finding

Let a finite drainage network be a rooted tree, with the outlet at the root. In the linear recession model below, the determinant of the complete outlet observability matrix has a closed factorization:

\[
\det\mathcal O = c^n\left(\prod_{v\ne r} g_v\right)
\prod_{\substack{i<j\\i\parallel j}}(k_i-k_j).
\]

Here \(i\parallel j\) means that neither vertex lies on the unique root-to-other path; \(g_v\) is the product of strictly positive downstream transfer coefficients along the root-to-\(v\) path, excluding the root. The labels are any fixed topological ordering with the root first. In particular, an ideal noiseless single outlet recession trace determines *every initial store* uniquely exactly when **no two incomparable stores have the same recession rate**. Coincident rates on a single ancestral chain do not destroy observability. If any incomparable rates coincide, distinct strictly positive initial-storage vectors can have the same entire outlet trace.

This is an exact, all-network-size result, not a generic-rate assertion. The complete \(n\)-entry outlet derivative jet through order \(n-1\) suffices when observable; a shorter derivative jet cannot uniquely determine arbitrary \(n\)-dimensional initial states.

## Assumptions and scope

Let \(T=(V,E)\) be a finite rooted tree with \(|V|=n\ge1\), root \(r=0\), and a topological labeling \(V=\{0,1,\ldots,n-1\}\) such that every parent has lower index than its children. Each vertex \(v\) has a *known* total linear depletion rate \(k_v>0\). For every nonroot vertex \(v\), the flux from \(v\) into its parent has a known transfer rate \(b_v>0\), with \(b_v\le k_v\) in the passive water-conserving interpretation; the remainder \(k_v-b_v\) represents other loss. After a prior recharge event has ended, no further external input enters. The vector of stored volumes satisfies

\[
\dot x_v=-k_vx_v+\sum_{u:\operatorname{parent}(u)=v}b_ux_u,
\qquad x(0)=\xi\in[0,\infty)^n.
\]

The observed downstream outlet flux is \(y(t)=c x_r(t)\), where the known outlet coefficient satisfies \(c>0\) (physically one may set \(c=k_r\)). All coefficients and the tree topology are assumed known, and the exact continuous trace is observed on a nonempty open time interval. The unknowns in the theorem are only the \(n\) initial storage volumes.

Define the matrix \(A\) by \(A_{vv}=-k_v\), \(A_{\operatorname{parent}(v),v}=b_v\) for \(v\ne r\), and all other entries zero; let \(C=c e_r^{\mathsf T}\). The observability matrix is

\[
\mathcal O=\begin{pmatrix}C\\CA\\\vdots\\CA^{n-1}\end{pmatrix}.
\]

Let \(P(v)\) be the root-to-\(v\) vertex path, endpoints included, and put \(g_r=1\), \(g_v=\prod_{u\in P(v)\setminus\{r\}}b_u\). The product over incomparable index pairs is empty, and equals one, for a chain or a one-vertex tree.

## Proof

**Step 1: exact transfer numerators.** The triangular differential system has characteristic polynomial

\[
\chi(s)=\det(sI-A)=\prod_{u\in V}(s+k_u).
\]

Starting with unit storage at one vertex \(v\), flux propagates solely along its unique downstream path; repeated scalar resolvent elimination gives

\[
C(sI-A)^{-1}e_v=\frac{c g_v}{\prod_{u\in P(v)}(s+k_u)}.
\]

Thus the \(v\)-th polynomial numerator, after multiplication by the common denominator \(\chi\), is

\[
p_v(s)=c g_v\prod_{u\notin P(v)}(s+k_u),
\quad\deg p_v\le n-1.
\]

This formula remains valid with repeated rates; no partial-fraction or distinct-eigenvalue hypothesis was made.

**Step 2: numerators have the same determinant as the derivative-jet matrix.** Write the exact initial-state outlet transform as \(Y(s)=\sum_v\xi_v p_v(s)/\chi(s)\). For large \(s\),

\[
Y(s)=\frac{y(0)}s+\frac{y'(0)}{s^2}+\cdots+
\frac{y^{(n-1)}(0)}{s^n}+O(s^{-n-1}).
\]

Since \(\chi\) is monic of degree \(n\), the coefficients of \(\chi(s)Y(s)\) in descending powers \(s^{n-1},\ldots,s^0\) are related to the jet \((y(0),\ldots,y^{(n-1)}(0))\) by a lower-triangular transformation with all diagonal entries one. Consequently, the matrix whose columns are the descending coefficients of the polynomials \(p_v\) has determinant exactly \(\det\mathcal O\).

**Step 3: leaf deletion and exact factorization.** Induct on \(n\). For \(n=1\), the numerator coefficient matrix is \((c)\), and the asserted determinant equals \(c\). For \(n>1\), the largest-labeled vertex \(\ell=n-1\) is a leaf. Delete it, and denote the smaller-tree numerator polynomials by \(p_v^{\rm old}\). Every remaining polynomial is

\[
p_v^{\rm new}(s)=(s+k_\ell)p_v^{\rm old}(s),\qquad v\ne\ell.
\]

On degree-at-most-\(n-1\) polynomials, replace the descending monomial coefficients by the descending coefficients of the quotient upon monic division by \(s+k_\ell\), followed by the remainder \(f(-k_\ell)\). Synthetic division shows that this change of coordinates has determinant one. The first \(n-1\) transformed numerator columns therefore consist of the old coefficient columns and a zero last entry. Expanding along that last row gives

\[
\det\mathcal O_{\rm new}
=\det\mathcal O_{\rm old}\,p_\ell^{\rm new}(-k_\ell).
\]

Because \(\ell\) is a leaf, every vertex not on \(P(\ell)\) is incomparable with \(\ell\). Hence

\[
p_\ell^{\rm new}(-k_\ell)=c g_\ell
\prod_{\substack{i<\ell\\i\parallel\ell}}(k_i-k_\ell).
\]

Iterating the identity proves the stated product formula, including its sign for the specified topological ordering.

**Step 4: identifiability and sharpness.** The exact analytic trace is \(y(t)=C e^{At}\xi\). It determines the first \(n\) derivatives at zero, whose coefficient matrix in \(\xi\) is \(\mathcal O\). When the product is nonzero, the initial state is uniquely reconstructed by this finite linear system. When it is zero, choose any nonzero \(h\in\ker\mathcal O\). Cayley–Hamilton implies \(CA^jh=0\) for every nonnegative integer \(j\), hence \(C e^{At}h=0\) for all \(t\ge0\). Taking an arbitrary strictly positive baseline \(\xi\) and a sufficiently small nonzero \(\varepsilon\) yields two distinct strictly positive vectors \(\xi\) and \(\xi+\varepsilon h\) with identical entire traces. Finally, fewer than \(n\) scalar derivatives give a linear map into a space of dimension below \(n\) and cannot identify arbitrary initial states.

## Verification

The included standalone script `check_observability.py` uses exact arithmetic in SymPy. It recomputes the observability matrix and independently checks the displayed product against symbolic determinants for all 34 parent-topologically ordered rooted trees through five vertices. It additionally checks 665 seeded exact-rational tree/rate/transfer instances with two through eight vertices, including 105 singular cases, and four explicit repeated-rate chain/branch boundary cases.

For a three-store star with root \(0\) and upstream children \(1,2\), the determinant is \(c^3b_1b_2(k_1-k_2)\), so equal child depletion rates prevent recovery of the two individual stores. For the three-store chain \(0\leftarrow1\leftarrow2\), the determinant is \(c^3b_1^2b_2\) even when all three depletion rates coincide. These are structural examples, not substitutes for the all-tree proof.

Run from a directory containing the script using `python check_observability.py` with Python 3 and SymPy. Checks are finite corroboration; the preceding exact induction proves the infinite family.

## Relationship to prior work

Nash's 1957 instantaneous unit hydrograph develops series of linear reservoirs. Pan and Wood's public 2013 inverse-routing study studies spatially distributed runoff estimation from gauged streamflow, with a different routing operator and unknown time-varying inputs. This result instead assumes known tree rates and *no new inputs* and addresses whether a single output trace identifies initial storage; it neither disputes nor implies the feasibility of reconstructing arbitrary changing runoff fields from one outlet gauge.

Prior compartmental-systems literature develops generic structural observability (Cobelli, Lepschy and Romanin-Jacur, 1979) and visible or hidden repeated eigenvalue modes (Fagarasan and DiStefano, 1986). Those general concepts may encompass the qualitative equal-rate obstruction. The specific claim here is the explicit all-tree, all-positive-transfer **determinant product** and its exact, topology-indexed zero factors. The accessible 1986 abstract does not exhibit this product; its full article was unavailable for direct comparison, so historical priority remains subject to that risk. A published result on endpoint observation of normalized paths concerns a different symmetric graph evolution and does not imply this directed-tree product. No assertion of independently certified novelty is made.

## Limitations

This theorem concerns deterministic, linear, finite, rooted, acyclic routing with known coefficients and noiseless continuous outlet observation after forcing has stopped. It does not estimate unknown rates, arbitrary unknown rainfall/runoff input signals, nonlinear channel dynamics, travel-time delays, or measurement error. Analytic differentiation can be severely unstable with noisy observations even if the determinant is nonzero. The determinant measures exact algebraic singularity; it is not a standalone bound for statistical estimation error. The 1986 compartmental observability literature was not fully available for a priority comparison. The earliest day-resolved public motivating source used for the dated scope is Pan and Wood's 3 June 2013 discussion paper; this does not assert that Nash's 1957 reservoir model first appeared in 2013.

## References

1. Nash, J. E. (1957), *The form of the instantaneous unit hydrograph*, International Association of Hydrological Sciences General Assembly, Toronto, pp. 114–121. https://iahs.info/uploads/dms/045011.pdf .
2. Pan, M. and Wood, E. F. (2013), *Inverse streamflow routing*, Hydrology and Earth System Sciences **17**, 4577–4588; discussion version publicly available on 3 June 2013. https://doi.org/10.5194/hess-17-4577-2013 .
3. Cobelli, C., Lepschy, A. and Romanin-Jacur, G. (1979), *Identifiability of compartmental systems and related structural properties*, Mathematical Biosciences. https://doi.org/10.1016/0025-5564(79)90026-9 .
4. Fagarasan, J. T. and DiStefano, J. J. (1986), *Hidden pools, hidden modes and visible repeated eigenvalues in compartmental models*, Mathematical Biosciences **82**, 87–114. https://doi.org/10.1016/0025-5564(86)90006-4 .
