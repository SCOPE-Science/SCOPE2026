# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The proof was checked independently at the level of each implication.

- The essential-spectral-tail lemma is valid for arbitrary \(C\in B(H)\): a
  finite-rank projection \(1_{(t,\infty)}(|C|)\) would give a finite-rank
  approximation to \(C\) within \(t<\|C\|_{\mathrm e}\), a contradiction.
- The input witnesses are explicit rank-one column or row spaces. Their
  complementability is verified by contractive maps of the form
  \(X\mapsto P_MXP_z\) or \(X\mapsto P_yXP_M\); it is not inferred from an
  unconditional basis.
- The output witness used for Kolmogorov numbers is also 1-complemented.
  Closedness of \(A(M)\), or of the corresponding \(B^*\)-image, follows from
  the uniform lower bound on the spectral-tail subspace.
- The approximation-number lower bound uses the kernel of a finite-rank
  perturbation; the Bernstein bound uses finite-dimensional subspaces of the
  witness; the Gelfand bound uses intersection with finite-codimensional
  subspaces; the Kolmogorov bound uses a contractive projection onto the
  Hilbertian output witness followed by orthogonality to the projected target.
- For distance to strictly singular operators, strict singularity on the whole
  ideal forces arbitrarily small values on the infinite-dimensional witness.
  The inclusions
  \(\mathcal K\subset\mathcal{FSS}\subset\mathcal{SS}\) then give the other
  distance lower bounds.
- If one coefficient is compact, replacing the other modulo compact operators
  produces a compact two-sided multiplier. Approximating both compact
  coefficients by finite-rank operators gives the finite-rank perturbations
  needed for all four asymptotic upper bounds.
- For one-sided multiplication, \(\|I\|_{\mathrm e}=1\), so the universal
  lower bound equals the full multiplier norm. This forces exact equality for
  every finite index and exact equality for all three ideal distances.

No hidden compactness, duality, or complementability assumption was used.

## Originality — PASS

The originality claim is deliberately narrower than the qualitative
strict-singularity statement.

Lindström–Saksman–Tylli (2005) treat strict singularity and cosingularity of
two-sided multiplication on \(L(X)\). Their Fact 2.1 explicitly says that the
basic strict-singularity implications also hold for restrictions to compact
operator spaces. Vala's compactness theorem and later multiplication-operator
literature likewise make the qualitative compact/strict-singular boundary
prior-art-adjacent. Those facts are treated as prior art here.

Fialkow–Loebl (1984) study elementary mappings into ideals of operators.
Mathieu–Tradacete (2020) study strict singularity on full operator algebras.
Huang–Sukochev–Xu–Zhu (2026) give exact norm and range criteria for
multiplication from a semifinite factor into a symmetrically normed operator
space. Searches using exact and synonymous formulations did not locate the
all-index identities for approximation, Bernstein, Gelfand and Kolmogorov
numbers of one-sided multipliers acting on a symmetric norm ideal, the exact
distances to \(\mathcal K,\mathcal{FSS},\mathcal{SS}\), or the two-sided
essential-norm floor and one-compact-factor asymptotic formula.

Residual risk remains because the elementary-operator and norm-ideal
literature is large, and an older equivalent quantitative statement under
different terminology cannot be excluded. Originality is therefore asserted
only to the best of our knowledge.

## Value — PASS

The result gives a sharp and uniform obstruction to every standard form of
finite-dimensional approximation or strict singularity for one-sided
multiplication on a broad class of operator ideals. The exact flatness is
notably strong even when the coefficient \(A\) is rank one: \(L_A\) still has
all four classical \(s\)-numbers equal to \(\|A\|\). The same rank-one witness
mechanism also produces a quantitative two-sided essential-norm floor and
exact compact-factor asymptotics, making the argument reusable beyond the
one-sided corollary.

## Limitations checked

The result is not asserted for quasi-Banach ideals, nonsymmetric operator
spaces, or finite sums of elementary operators. For two noncompact
coefficients the lower floor \(\mu(A,B)\) is not claimed to be the exact
finite-index profile or exact ideal distance.
