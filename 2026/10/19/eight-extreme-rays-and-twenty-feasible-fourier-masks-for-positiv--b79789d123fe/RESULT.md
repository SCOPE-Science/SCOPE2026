# Eight extreme rays and twenty feasible Fourier masks for positive six-point Walsh signals

## Finding
Let \(G=\mathbb F_2^d\), \(d\ge3\), and let \(H\le G\) be a three-dimensional linear subgroup. Fix distinct nonzero \(a,b\in H\), and let \(S=H\setminus\{a,b\}\). Thus \(S\) has exactly six elements and contains the identity. Among functions with **exact** spatial support \(S\), impose the two simultaneous pointwise constraints \(f\ge0\) and \(\widehat f\ge0\), where \(\widehat f\) is the Walsh transform.

Identify \(H\cong\mathbb F_2^3\) so that \(a=1\) and \(b=2\), using binary coordinates \(0,\ldots,7\). A hexadecimal mask \(m\in\{01,\ldots,\mathrm{ff}\}\) represents precisely those local frequencies \(j\) for which its bit \(j\) is one. **Exactly twenty** masks occur:

| Local Fourier-support cardinality | Attainable masks |
|:--:|:--|
| 3 | `89` |
| 4 | `99` |
| 5 | `8f`, `ad`, `cb`, `e9` |
| 6 | `9f`, `af`, `bd`, `cf`, `db`, `eb`, `ed`, `f9` |
| 7 | `bf`, `df`, `ef`, `fb`, `fd` |
| 8 | `ff` |

In particular the attainable **global** Fourier-support cardinalities, for every \(d\ge3\), are exactly
\[
\boxed{\{3,4,5,6,7,8\}\,2^{d-3}}.
\]
The normalized feasible spectral-weight polytope in dimension eight has precisely eight vertices, yielding the complete support-mask classification by convex geometry, not only a cardinality bound.

## Assumptions and scope
The unnormalized Walsh transform is
\[
\widehat f(\xi)=\sum_{x\in G}f(x)(-1)^{\langle\xi,x\rangle}.
\]
Both positivity conditions are pointwise, with zero permitted at the specified missing spatial positions and at non-retained frequencies, while **all** values at the six retained spatial positions and **all** values at the retained frequencies must be strictly positive. For the local eight-point calculation, normalize the nonnegative Fourier vector \(t\) by \(\sum_jt_j=1\). The inverse Walsh transform is \(f(x)=\tfrac18\sum_j(-1)^{x\cdot j}t_j\), so its support is unaffected by the factor \(1/8\).

All masks use the fixed coordinate convention. For other bases of \(H\) taking the missing pair to \(1,2\), masks are relabelled by the corresponding dual linear map. The set and number of feasible masks are basis independent.

## Proof
**(1) Reduction to eight points.** Since \(f\) is supported inside \(H\), its transform at \(\xi\in\widehat G\) depends only on the restriction of \(\xi\) to \(H\). The restriction map onto \(\widehat H\) is surjective with \(2^{d-3}\) characters above each local frequency. Thus all Fourier supports are the inverse images of local masks; conversely every local admissible example extends by zero outside \(H\). The two removed nonzero elements are linearly independent, so an automorphism of \(H\) takes them to \(1,2\).

**(2) A compact rational polytope.** Write \(W_{xj}=(-1)^{x\cdot j}\), indexed by binary integers. Put \(R=\{0,3,4,5,6,7\}\). Exactly the normalized vectors
\[
P=\bigl\{t\in\mathbb R^8:\ t_j\ge0,\ \sum_jt_j=1,\ (Wt)_1=(Wt)_2=0,\ (Wt)_x\ge0\ (x\in R)\bigr\}
\]
are allowed before imposing strict spatial positivity. It is bounded. Every vertex is a basic feasible solution of the three equalities together with five linearly independent active inequalities among eight frequency inequalities and six spatial inequalities. There are exactly \(\binom{14}{5}=2002\) possible choices of five. The supplied exact rational Gaussian-elimination certificate checks **every** choice, skips singular systems, evaluates all inequalities exactly, and obtains precisely the following eight vertices:

| Fourier mask | Positive Fourier coordinates and common weight |
|:--|:--|
| `09` | \(0,3\), each \(1/2\) |
| `81` | \(0,7\), each \(1/2\) |
| `0f` | \(0,1,2,3\), each \(1/4\) |
| `69` | \(0,3,5,6\), each \(1/4\) |
| `99` | \(0,3,4,7\), each \(1/4\) |
| `a5` | \(0,2,5,7\), each \(1/4\) |
| `c3` | \(0,1,6,7\), each \(1/4\) |
| `ff` | all eight coordinates, each \(1/8\) |

These are indeed vertices: the certificate establishes that each is an actual full-rank basic feasible solution, not just a feasible point. Every vertex must occur in the enumeration by the active-constraint theorem: \(P\) is a full-dimensional polytope relative to its five-dimensional equality affine hull, as witnessed by the strictly positive feasible point constructed below.

**(3) Exact strict-mask criterion.** For any candidate frequency mask \(T\subseteq\{0,\ldots,7\}\), let \(V_T\) be the subset of the eight vertices with support contained in \(T\). A point of \(P\) with exact spectral support \(T\) and strictly positive six retained spatial values exists if and only if (a) for every \(j\in T\) at least one vertex of \(V_T\) has \(t_j>0\), and (b) for each \(x\in R\) at least one vertex of \(V_T\) has \((Wt)_x>0\). Necessity follows from nonnegativity and convex decomposition into vertices. For sufficiency, average all vertices of \(V_T\); no nonnegative linear coordinate can cancel in this average, so each required coordinate is positive and all excluded coordinates vanish. This proves the logical correctness of the finite test **independently** of its numerical output.

The exact checker evaluates this criterion for all \(255\) nonempty masks and returns exactly the twenty masks in the displayed table, with cardinality distribution \(1,1,4,8,5,1\). It also constructs and checks a rational strictly positive witness for each of them by averaging compatible vertices. In particular `ff` is strictly feasible, so the polytope has the expected five-dimensional affine hull. The listed masks are therefore attainable and every unlisted mask is impossible.

## Verification
The standalone Python 3 standard-library checker `artifacts/verify.py` builds the Walsh matrix, performs all \(2002\) eight-by-eight rational systems using exact `fractions.Fraction` arithmetic, asserts the full eight-vertex list, tests every one of \(255\) nonempty spectral masks by the proved averaging criterion, validates a rational primal witness for each of the twenty accepted masks, and prints `VERIFY_OK`. Its checked output gives the six mask rows exactly as displayed. No floating-point tolerance, external solver, partial sampling, or unverified symbolic identity is involved.

## Relationship to prior work
Meshulam's finite-abelian uncertainty inequality (2003 preprint) supplies support-size lower bounds without two-sided positivity, positional support-mask feasibility, or this eight-point polytope. Krahmer, Pfander, and Rashkov (2006 preprint) display unrestricted complex-valued Fourier-support size diagrams, including the order-eight Boolean group, but their relevant Section 3 and Figure 3 do not classify Fourier supports under simultaneous spatial and Fourier nonnegativity. Those general statements neither rule out the two hundred thirty-five forbidden **positional** masks nor imply the eight-vertex structure.

A published exact-support four theorem for Boolean groups gives structural patterns for four, rather than six, arbitrary complex nonzero spatial coefficients. Another published order-eight incidence table concerns the **cyclic group** \(\mathbb Z_8\), unrestricted complex coefficients, rather than \(\mathbb F_2^3\) with pointwise positivity. Neither subsumes the present normalized convex cone or its exact twenty masks. Further comparisons and residual literature risks are recorded in `AUDIT.json`.

## Limitations
The explicit positional mask table pertains to the specific six-point orbit \(H\setminus\{a,b\}\) and requires both nonnegativity conditions. It does not classify arbitrary six-point sets of affine span exceeding three, higher-group orders beyond the stated subgroup extension, or spectral amplitudes beyond their feasible support patterns. An earlier equivalent convex-cone tabulation under a different name remains an originality risk. Independent mathematical validation has not been carried out.

## References
1. R. Meshulam, *An uncertainty inequality for finite abelian groups*, arXiv:math/0312407, first submitted 2003-12-22. Relevant theorem and Section 2 inspected in the freely available complete seven-page paper.
2. F. Krahmer, G. E. Pfander, and P. Rashkov, *Uncertainty in time--frequency representations on finite Abelian groups and applications*, arXiv:math/0611493, first submitted 2006-11-16, especially Section 3 and Figure 3.
3. *Four-sparse Walsh spectra are controlled by affine dimension on \(\mathbb F_2^d\)*, published published-finding corpus claim `2026/10/4/SCOPE-four-sparse-walsh-spectra-are-controlled-by-affine-dimension-on--1491c27461f4`, full RESULT.md inspected for mathematical overlap.
4. *Support-pattern incidence refinement of the order-eight Fourier uncertainty diagram*, published published-finding corpus claim `2026/10/4/SCOPE-support-pattern-incidence-refinement-of-the-order-eight-fourier--78caf4d7929b`, full RESULT.md inspected for mathematical overlap.
