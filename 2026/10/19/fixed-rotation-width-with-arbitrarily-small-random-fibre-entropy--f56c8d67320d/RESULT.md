# Fixed rotation width with arbitrarily small random fibre entropy

## Finding

**Theorem (fixed-width rare-event family).** For every \(\Delta>0\) and every integer \(K>\Delta/2\), put \(p=\Delta/(2K)\). Take the independent two-symbol Bernoulli base with symbol-one probability \(p\). On \(\mathbb S^1=\mathbb R/\mathbb Z\), use the identity map on symbol zero and the real-analytic degree-one endomorphism induced by the lift
\[
G_K(x)=x+K\sin(2\pi x)
\]
on symbol one. For almost every driving sequence, the random rotation set (defined through lift displacement as in Li–Lloyd–Romaña) is exactly
\[
\operatorname{Rot}(G)=[-\Delta/2,\Delta/2].
\]
The sample/fibre random topological entropy obeys the **exact time-change identity**
\[
h_{\rm top}^{(r)}=p\,h_{\rm top}(g_K),\qquad g_K=G_K\pmod1,
\]
and the fully explicit bounds
\[
\frac{\Delta}{2K}\log(K+1)\;\le\;h_{\rm top}^{(r)}\;\le\;\frac{\Delta}{2K}\log(1+2\pi K).
\]
In particular, the random entropy is strictly positive for each \(K\), but tends to zero as \(K\to\infty\), although its random rotation-set diameter stays identically \(\Delta\). Thus **no strictly positive universal lower bound for fibre random topological entropy can be a function solely of the positive diameter of the random rotation set**, even for an iid two-map system with real-analytic degree-one circle maps.

## Assumptions and scope

The base is \(\Omega=\{0,1\}^{\mathbb N}\) with Bernoulli law \((1-p,p)\) and left shift. All entropy assertions concern *quenched/sample (fibre)* topological entropy, not the topological entropy of the full skew product or an annealed partition function. The lift of the zero-symbol map is \(I(x)=x\), and the lift of the one-symbol map is \(G_K\) above. A random \(n\)-step lift is the chronological composition of the first \(n\) lifts. The random rotation set is the almost-sure compact interval of accumulation velocities defined by Li, Lloyd and Romaña, arXiv:2606.16498, Theorem 2.1. The random fibre entropy is defined by \(\lim_{\varepsilon\downarrow0}\limsup_{n\to\infty}n^{-1}\log s(n,\varepsilon,\omega)\), where \(s\) is the maximal cardinality of an orbit-Bowen-separated set in \(\mathbb S^1\).

The parameter \(\Delta\) is any finite positive real number, and \(K\) is any positive integer with \(2K>\Delta\). Consequently \(0<p<1\). No uniform bound on the Lipschitz constants as \(K\) varies is assumed.

## Proof

**1. Lift displacement and extremal velocities.** The identity and \(G_K\) are degree-one real-analytic lifts, since \(G_K(x+1)=G_K(x)+1\). Every one-symbol step changes its current lifted coordinate by a number in \([-K,K]\), and a zero-symbol step does not change it. Writing \(N_n(\omega)=\sum_{j=0}^{n-1}\omega_j\), we have the exact cocycle identity
\[
G_\omega^{(n)}=G_K^{N_n(\omega)}.
\]
For all \(x\in\mathbb R\),
\[
-KN_n(\omega)\le G_\omega^{(n)}(x)-x\le KN_n(\omega).
\]
The strong law gives \(N_n/n\to p\) for almost every \(\omega\). Moreover, the two distinct circle points \(x_+=1/4\) and \(x_-=3/4\) satisfy \(G_K(x_+)=x_++K\) and \(G_K(x_-)=x_--K\). By the degree-one property, for each \(n\), the random lifted displacement at these points is respectively \(KN_n\) and \(-KN_n\). Thus both extremal velocities \(pK\) and \(-pK\) occur as actual limits, whereas no limsup, liminf, or subsequential velocity can fall outside \([-pK,pK]\). The interval theorem for integrable degree-one random circle endomorphisms over an ergodic base (Li–Lloyd–Romaña, Theorem 2.1) makes the almost-sure rotation set a compact interval. Hence it is precisely \([-pK,pK]=[-\Delta/2,\Delta/2]\). We use that theorem only for the interval property; the two endpoints and the enclosing bound were established directly.

**2. Exact entropy time change.** For the fixed driving sequence and for each \(j\ge0\), the circle map applied by time \(j\) is \(g_K^{N_j(\omega)}\). Since \(N_0=0\) and its increments belong to \(\{0,1\}\), the integers \(N_j\) with \(0\le j<n\) visit every integer from \(0\) through \(N_{n-1}\). Consequently the *entire sample Bowen metric*, not just its asymptotic behavior, is the deterministic Bowen metric of \(g_K\) for \(N_{n-1}+1\) observations. In particular,
\[
s(n,\varepsilon,\omega)=s_{g_K}(N_{n-1}(\omega)+1,\varepsilon).
\]
For almost every \(\omega\), \(N_{n-1}+1\to\infty\), \((N_{n-1}+1)/n\to p\), and the observation counts \(N_{n-1}+1\) eventually visit *every sufficiently large positive integer*. The last property is crucial when taking a limsup. Therefore, at each fixed scale,
\[
\limsup_{n\to\infty}\frac1n\log s(n,\varepsilon,\omega)
=p\limsup_{m\to\infty}\frac1m\log s_{g_K}(m,\varepsilon).
\]
Taking \(\varepsilon\downarrow0\) yields \(h_{\rm top}^{(r)}=p h_{\rm top}(g_K)\).

**3. Explicit lower entropy bound.** Let \(J=[0,1/4]\). On this interval, \(G_K'(x)=1+2\pi K\cos(2\pi x)\ge1\), and \(G_K\) maps \(J\) strictly increasingly onto \([0,K+1/4]\). For each integer \(j\in\{0,\ldots,K\}\), define the compact interval
\[
J_j=(G_K|_J)^{-1}([j,j+1/4]).
\]
These \(K+1\) intervals lie in \(J\) and are pairwise disjoint, with positive pairwise distances. Their images under the circle map \(g_K\) are all exactly \(J\) (modulo one). Iterated inverse branches therefore produce \((K+1)^n\) initial points with any prescribed \(n\)-letter itinerary through the \(J_j\). Two different itineraries are separated at their first differing observation time by at least the positive minimum gap between these intervals. Thus \(h_{\rm top}(g_K)\ge\log(K+1)\).

**4. Explicit upper entropy bound.** The circle map \(g_K\) has Lipschitz constant at most \(L_K=1+2\pi K\), because \(|G_K'|\le L_K\). Cover the unit circle by \(O(L_K^{n-1}/\varepsilon)\) arcs of length at most \(\varepsilon/L_K^{n-1}\). Each arc has deterministic \(n\)-step Bowen diameter at most \(\varepsilon\); hence \(h_{\rm top}(g_K)\le\log L_K\). Together with Step 3 and the exact time-change identity, this proves the displayed double inequality.

**5. Sharp qualitative consequence.** For fixed \(\Delta>0\), both displayed bounds are positive at every permitted \(K\) and the upper bound tends to zero as \(K\to\infty\). Thus any putative strictly positive lower-bound function depending only on the nonzero diameter \(\Delta\) is contradicted. The resulting entropy collapse is quantitatively of order \(\Delta\log K/K\), with unspecified multiplicative constants bounded by the explicit two-sided formula.

## Verification

The accompanying standalone script `verify.py` checks finite instances of the cylinder inverse-branch construction, symbolic observation-count identity, exact rational frequency normalization, and the analytic entropy bounds for several parameter choices. Run with `python3 verify.py` using only Python's standard library. These checks are consistency tests, not a replacement for the strong law, the cited random-rotation interval theorem, or the infinite-word horseshoe argument. The proof above supplies those universal steps.

## Relationship to prior work

Li, Lloyd and Romaña (2026), arXiv:2606.16498, prove that a positive random rotation-set width forces positive random fibre entropy (Theorem 2.3), and their Section 5, Question 2 discusses quantitative entropy estimates and the absence of a proved bound depending only on width. Their Bernoulli piecewise-affine example has entropy \(\log3\), independent of the driving parameter (Example 4.1). The present fixed-width analytic family proves a complementary *nonuniformity boundary*: without additional recurrence/regularity restrictions, no strictly positive universal width-only bound exists. It does not weaken their qualitative positivity theorem.

Classical work of Alsedà, Llibre, Mañosas and Misiurewicz (1988), and of Alsedà and Mañosas (1990), gives deterministic entropy estimates from rotation intervals. Those estimates apply to one deterministic circle endomorphism, not automatically to a random sequence with arbitrarily rare high-displacement episodes. The exact idle-step entropy identity is elementary, but its simultaneous combination with a fixed, arbitrarily prescribed random rotation-set width provides the parameter-level obstruction here.

## Limitations

The inactive generator is exactly the identity and the active generator has unbounded derivative as \(K\to\infty\). No assertion is made for a family with a uniform generator-Lipschitz cap, a fixed positive lower bound on active-event frequency, random Anosov systems, annealed entropy, or the entropy of the skew product including base randomness. The deterministic entropy \(h_{\rm top}(g_K)\) is bounded sharply enough for the qualitative conclusion, but its exact value is not calculated. Independent scientific review is not claimed.

## References

1. Z. Li, S. Lloyd, S. Romaña, *Rotation Sets and Topological Entropy for Random Circle Endomorphisms*, arXiv:2606.16498v1 (first public version 2026-06-15), especially Theorems 2.1 and 2.3, Example 4.1, and Section 5 Question 2. https://arxiv.org/abs/2606.16498
2. Z. Li, S. Lloyd, *Periodicity and Rotation Number for Random Circle Homeomorphisms*, arXiv:2603.18617v1 (2026-03-19), for the surrounding random-rotation framework. https://arxiv.org/abs/2603.18617
3. L. Alsedà, J. Llibre, F. Mañosas, M. Misiurewicz, *Lower bounds of the topological entropy for continuous maps of the circle of degree one*, Nonlinearity 1 (1988), 463–479. DOI:10.1088/0951-7715/1/3/004.
4. L. Alsedà, F. Mañosas, *Kneading theory and rotation intervals for a class of circle maps of degree one*, Nonlinearity 3 (1990), 413–452. DOI:10.1088/0951-7715/3/2/008.
