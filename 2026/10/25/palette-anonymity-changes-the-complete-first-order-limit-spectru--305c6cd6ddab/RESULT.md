# Palette anonymity changes the complete first-order limit spectrum of proper ternary paths

## Finding

Uniform proper ternary colourings of a long directed path have two different *complete arithmetic sets* of first-order limiting probabilities, depending on whether the palette has names. Let \(\mathcal L_{\rm named}\) denote the language with directed successor \(S\) and unary predicates \(P_1,P_2,P_3\), each position satisfying exactly one; let \(\mathcal L_{\rm anon}=\{S,E\}\), where \(E(x,y)\) means the two positions have the same colour. Equality of positions is available in both languages. For an integer \(n\ge2\), sample a ternary word of length \(n\) uniformly subject to different colours at adjacent positions; equivalently sample the named colouring from \(3\cdot2^{n-1}\) equiprobable possibilities. The anonymous structure is its image on forgetting the names but retaining \(E\). Each anonymous structure occurs with exactly six names, so this is also the uniform distribution on anonymous structures.

**Theorem.** For every fixed first-order sentence in either language, the satisfaction probability converges exponentially fast to an effectively computable limit. The complete sets of possible limits are
\[
\mathcal S_{\rm named}=\left\{\frac{a}{9\cdot2^m}:m\in\mathbb Z_{\ge0},\ 0\le a\le9\cdot2^m\right\},\qquad
\mathcal S_{\rm anon}=\left\{\frac{a}{3\cdot2^m}:m\in\mathbb Z_{\ge0},\ 0\le a\le3\cdot2^m\right\}.
\]
Here \(a\) is an integer. The containment \(\mathcal S_{\rm anon}\subsetneq\mathcal S_{\rm named}\) is strict: \(1/9\) belongs only to the named spectrum, while \(1/6\) is attained anonymously.

For uniform proper ternary colourings of a directed cycle of length \(n\ge3\), both languages have an effective **zero–one law** with exponential convergence. In contrast, for binary proper-coloured directed paths, a first-order sentence asking whether both endpoints have the same colour alternates deterministically with the parity of \(n\), in either language, so convergence fails.

## Assumptions and scope

The path is the structure with universe \(\{1,\ldots,n\}\) and \(S(i,j)\) iff \(j=i+1\). The cycle has \(S(i,j)\) iff \(j=i+1\) modulo \(n\). The colours form a fixed palette of size three and proper means unequal at every successor edge. There is no linear-order relation, no arithmetic, and no additional individual constants. In the anonymous language, \(E\) is an actual equivalence relation induced by a colouring; it is **not** an arbitrary independent relation. Both measures are taken *at fixed length* before sending \(n\) to infinity. For a fixed first-order sentence \(\varphi\), exponential convergence means there are computable constants \(C>0\) and \(0<\theta<1\), possibly depending on \(\varphi\), such that the difference from its limiting probability is at most \(C\theta^n\) for all sufficiently large \(n\).

## Proof

**1. Uniform paths are a primitive finite-state chain.** Generate the first colour uniformly in \(\{1,2,3\}\) and then choose each next colour uniformly among the other two. This gives precisely the uniform proper-colouring law. Its transition matrix is \(P=(J-I)/2\), where \(J\) is the three-by-three all-ones matrix. The exact identity
\[
P^t=J/3+(-1/2)^t(I-J/3)
\]
implies exponentially fast mixing. If \(u,v\) are any two proper length-\(L\) words and \(n\ge2L\), the probability of having prefix \(u\) and suffix \(v\) is
\[
\frac{1}{3\cdot2^{2(L-1)}}(P^{n-2L+1})_{u_L,v_1}.
\]
In particular, it converges to \(1/D_L^2\), where \(D_L=3\cdot2^{L-1}\). The convergence is exponentially fast and uniform over the finite list of \(D_L^2\) endpoint pairs.

**2. Internal patterns become saturated exponentially fast.** For each fixed proper word \(w\) of length \(h\), sample trial windows separated far enough that the first colour of the next trial follows the previously exposed state by two Markov steps. Every such trial has conditional probability bounded below by a positive constant \(\delta_w\), since \(P^2\) has all entries positive. By conditional binomial domination, for every fixed threshold \(T\), the probability that fewer than \(T\) of these disjoint windows equal \(w\) is at most \(C_w e^{-c_w n}\). There are finitely many proper \(h\)-words, so the same bound holds for failure of *simultaneous* saturation of all such words. This includes saturation of the full rooted-radius types away from the endpoints.

**3. First-order truth localizes to the endpoints.** In bounded-degree structures, the effective Hanf locality theorem gives, for each sentence \(\varphi\), a radius \(R\) and a threshold \(T\) such that the truth of \(\varphi\) depends only on counts of rooted radius-\(R\) neighbourhood types, truncated at \(T\). For a sufficiently long directed path, every interior type is a properly coloured window of length \(2R+1\), and all occur at least \(T\) times off an event of exponentially small probability, by Step 2. The unsaturated types meeting the two physical endpoints are completely determined by an \(L\)-letter prefix and an \(L\)-letter suffix, with \(L=\max(2,2R+1)\). Therefore there is a finite Boolean function \(F_\varphi(u,v)\) of legal endpoint words such that, outside an exponentially rare event, the word satisfies \(\varphi\) exactly when \(F_\varphi(u,v)=1\). Step 1 yields
\[
\Pr(W_n\models\varphi)=k_\varphi/D_L^2+O_\varphi(e^{-c_\varphi n}),
\qquad k_\varphi\in\{0,\ldots,D_L^2\}.
\]
The finite locality parameters and the function \(F_\varphi\) are computable, for instance by enumerating saturated finite witnesses with prescribed endpoints and using ordinary finite model checking. Since \(D_L^2=9\cdot2^{2(L-1)}\), this proves the named-spectrum **upper bound**.

**4. Every named-palette fraction occurs.** Any fixed legal prefix and suffix of length \(L\) can be specified by a first-order sentence using the successor relation and unary colour predicates. Their intersection has limit \(1/D_L^2\). These \(D_L^2\) events are pairwise exclusive for large \(n\), and disjunctions of arbitrary selections realize every numerator between zero and \(D_L^2\). Increasing \(L\) clears any additional power of two, giving exactly \(\mathcal S_{\rm named}\).

**5. Colour anonymity creates an exact orbit factor.** Every \(\mathcal L_{\rm anon}\)-sentence has an equivalent named-palette sentence obtained by replacing \(E(x,y)\) with \(\bigvee_{j=1}^3(P_j(x)\wedge P_j(y))\). Its truth is invariant under simultaneous permutation of the three palette labels. Hence, on the saturated event from Step 3, the endpoint function \(F_\varphi(u,v)\) is constant on orbits of the diagonal action of the six-element permutation group on proper endpoint pairs \((u,v)\). Since \(L\ge2\), the word \(u\) itself uses at least two different colours. A permutation fixing \(u\) pointwise must fix two of the three colours and therefore also the third. Thus this action is **free**: every orbit has precisely six pairs. It follows that \(6\mid k_\varphi\), and
\[
\lim_{n\to\infty}\Pr(W_n\models\varphi)
=\frac{6b_\varphi}{9\cdot2^{2L-2}}
=\frac{b_\varphi}{3\cdot2^{2L-3}}.
\]
Conversely, each orbit is exactly characterized by the finite equality pattern among the first and last \(L\) positions: two tuples of three-colour values are in the same palette-permutation orbit if and only if all their pairwise equality comparisons agree. That condition is expressible in \(\{S,E\}\) by quantifying the unique endpoint successor chains of length \(L\), then listing the required \(E\)-equalities and inequalities. The \(D_L^2/6=3\cdot2^{2L-3}\) orbit conditions are disjoint, with equal limiting probability \(1/(3\cdot2^{2L-3})\). Arbitrary disjunctions yield every numerator at that denominator; letting \(L\) increase produces exactly \(\mathcal S_{\rm anon}\). In particular, \(1/9\notin\mathcal S_{\rm anon}\), since \(3\) never divides a power of two; \(1/6\) arises by taking one orbit at \(L=2\).

**6. Cycles and the binary boundary.** A uniformly proper ternary directed cycle is the stationary Markov chain above conditioned on the last colour differing from the first; the conditioning event has probability bounded away from zero, because
\[
\#\{\text{proper ternary colourings of the cycle}\}=2^n+2(-1)^n.
\]
The pattern-saturation bound from Step 2 therefore remains exponential under conditioning. For fixed \(R,T\), every possible rooted neighbourhood type occurs at least \(T\) times with exponentially high probability, and cycles have no endpoints. Hanf locality makes the truth of every sentence eventually constant off this exponentially rare event. Translating \(E\) into unary colours proves the anonymous zero–one statement too. Finally, for binary paths the only words are the two alternating ones, and the endpoint equality statement holds exactly when \(n\) is odd; it is expressible in both languages.

## Verification

The standalone script `proper_colour_symmetry_checker.py` enumerates all proper words up to ten positions on the ternary palette, up to nine on the binary and quaternary palettes, and up to seven on the five-colour palette. It verifies exact endpoint transition counts, two-letter prefix/suffix counts, and the chromatic count of proper cyclic words. It additionally enumerates palette-permutation orbits for endpoint lengths two through six, checking that every ternary orbit has cardinality six and that the count of orbits equals \(D_L^2/6\). The successful signal is `PROPER_COLOUR_SYMMETRY_EXACT_OK 5090 69742 2046`. These exhaustive finite tests corroborate exact finite identities; the infinite logical convergence and spectrum assertions follow from the separate locality and probability proof, not finite extrapolation.

## Relationship to prior work

Marström and Räty, *Logical isomorphism and logical limit laws for small permutation classes and regular languages* (2026, arXiv:2610.22218, first posted October 15, 2026), motivate asking for full limiting-probability spectra in regular-language models. Their principal statements transfer limit laws from regular words to small permutation classes and do not give this anonymous-versus-named exact arithmetic spectrum for proper ternary path words. The first-order characterization of successor string languages by locally threshold testable languages is classical, credited to Thomas and recorded explicitly by Rocha, Martins and Ferreira; its local-normal-form idea underpins Step 3. Ahlman and Koponen study forgetting colouring labels in quite different dense/pregeometric random structures and obtain zero–one laws there, rather than the nontrivial rational path spectra here. The transfer identity and free-orbit calculation above are specific to the uniform proper ternary chain; the result does not assert novelty for classical Hanf locality, Markov mixing, or orbit counting in isolation.

## Limitations

The proof requires exactly three available colours and an irreflexive immediate-successor constraint. The spectra refer to ordinary first-order logic, not first-order logic enriched with full linear order, counting, arithmetic, or monadic second-order quantifiers. The anonymous language **retains same-colour equivalence**; forgetting colours completely would be a different model. The analogues for arbitrary larger unnamed palettes can have nonfree boundary orbits and are not classified here. The use of published locality and formal-language normal forms is essential, and historical priority remains subject to further specialist scrutiny.

## References

1. K. Marström and E. Räty, *Logical isomorphism and logical limit laws for small permutation classes and regular languages*, arXiv:2610.22218 (2026). https://arxiv.org/abs/2610.22218
2. T. A. Rocha, A. T. Martins, and F. M. Ferreira, *On Finding a First-Order Sentence Consistent with a Sample of Strings*, arXiv:1809.03106 (2018). https://arxiv.org/abs/1809.03106
3. W. Thomas, *Classifying regular events in symbolic logic*, Journal of Computer and System Sciences 25 (1982), 360–376. https://doi.org/10.1016/0022-0000(82)90016-2
4. O. Ahlman and V. Koponen, *Random l-colourable structures with a pregeometry*, Mathematical Logic Quarterly 63 (2017), 32–58; arXiv:1207.4936. https://arxiv.org/abs/1207.4936
5. L. Libkin, *Elements of Finite Model Theory*, Springer, 2004; standard effective Hanf locality theorem for bounded-degree relational structures.
