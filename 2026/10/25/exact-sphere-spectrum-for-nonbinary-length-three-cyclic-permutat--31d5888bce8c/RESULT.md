# Exact sphere spectrum for nonbinary length-three cyclic permutation bursts

## Finding
Fix an alphabet of size \(q\ge2\), an integer \(n\ge3\), and a word \(x\in\Sigma_q^n\). Let \(\mathcal B_3(x)\) consist of \(x\) itself and all distinct words obtained by cyclically rotating one non-wrapping length-three factor once or twice. These are **exact-length-three** bursts, not the union of shorter burst lengths.

Define \(H(x)\) to be the number of constant length-three factors. Define \(K(x)\) to be the number of length-four factors \(abcd\) with \(b\ne c\) and \(a,d\in\{b,c\}\). Then, for every such \(q,n,x\),
\[
|\mathcal B_3(x)|=2n-3-2H(x)-K(x).
\]

Let \(E_{q,n}(t)=\sum_{x\in\Sigma_q^n}t^{2H(x)+K(x)}\). With
\[
v_q(t)=\big(q(t^2+q-1),\;2q(q-1),\;q(q-1)(q-2)\big),\qquad
M_q(t)=\begin{pmatrix}t^2&q-1&0\\t&t&q-2\\1&1&q-2\end{pmatrix},
\]
the complete **distinct-output sphere-size distribution**, valid for every \(q\ge2,n\ge3\), is
\[
E_{q,n}(t)=v_q(t)M_q(t)^{n-3}\begin{pmatrix}1\\1\\1\end{pmatrix},\qquad
\sum_{x\in\Sigma_q^n}u^{|\mathcal B_3(x)|}=u^{2n-3}E_{q,n}(u^{-1}).
\]
In particular every coefficient of the right-hand side is an exact finite-length population, not a bound or approximation.

For every \(q\ge3\), the maximum sphere size is \(2n-3\), attained **exactly** by words having no constant length-three factor and no length-four factor of the above \(K\)-type. Writing \(F_q(n)\) for the number of maximizing words, their complete length enumerator is
\[
\sum_{n\ge3}F_q(n)z^{n-3}=
\frac{q(q-1)\big(q+1+(2q-3)z+q(q-2)z^2\big)}
{1-(q-2)z-(q-2)z^2-(q-1)(q-2)z^3}.
\]
For uniformly random \(X\in\Sigma_q^n\), the exact mean is
\[
\mathbb E|\mathcal B_3(X)|=2n-3-\frac{2(n-2)}{q^2}-\frac{4(n-3)(q-1)}{q^3}.
\]

For the four-letter alphabet at input length six, the complete sphere-size population polynomial is
\[
4u+24u^3+60u^4+132u^5+312u^6+720u^7+972u^8+1872u^9.
\]
Its coefficients sum to \(4^6=4096\), and 1872 words attain the sharp sphere size nine.

## Assumptions and scope
The alphabet consists of \(q\) distinct named symbols; no field structure or probability measure is needed for the counting theorem. A burst acts on exactly one contiguous length-three interval without wrapping around the endpoints of the full word. The permitted local permutations are exactly the identity and the two three-cycles; duplicate resulting words are counted only once. In the extremal theorem \(q\ge3\) is essential to construct a word all of whose consecutive triples have three distinct symbols; the spectrum identity itself holds for \(q=2\).

## Proof
**1. Local output counts and collisions.** Every nonconstant three-letter factor has exactly two distinct nonidentity cyclic rotations. A constant triple has none. Before deduplicating outputs arising from different windows, the number is therefore \(1+2(n-2-H(x))\). Any nonidentity permutation of a finite word changes at least two symbol positions. Two length-three windows at distance at least two overlap in at most one position and hence cannot yield the same nonidentity output. Two consecutive windows share precisely the central adjacent pair \(bc\); a common output must swap those two unequal letters and leave all others fixed. For the left triple \(abc\), this adjacent swap is produced by exactly one cyclic rotation if and only if \(a\in\{b,c\}\). For the right triple \(bcd\), it is produced by exactly one cyclic rotation if and only if \(d\in\{b,c\}\). Thus a duplicate exists exactly when \(b\ne c\) and \(a,d\in\{b,c\}\), and then it contributes precisely one duplicate. This cannot occur among three different windows because an adjacent pair belongs to at most two length-three intervals. Subtracting the \(K(x)\) duplicates proves the sphere formula without any unexplained inclusion-exclusion terms.

**2. Three-state weighted transfer.** After reading the first three letters \(abc\), record one of three states: \(T\) if \(b=c\), \(S\) if \(b\ne c\) and \(a\in\{b,c\}\), and \(D\) if \(a,b,c\) are pairwise distinct. The first triple has weight \(t^2\) precisely when it is constant. The weighted initial populations are \(q(t^2+q-1)\), \(2q(q-1)\), and \(q(q-1)(q-2)\), respectively.

For a new symbol \(d\), a fresh constant triple \(bcd\) adds defect two, and a new length-four collision pattern \(abcd\) adds defect one. Starting in \(T\), appending \(d=c\) gives \(T\) with weight \(t^2\), while the other \(q-1\) letters give \(S\) with weight one. Starting in \(S\), the choices \(d=c\) and \(d=b\) give \(T\) and \(S\), respectively, each with weight \(t\), while the other \(q-2\) choices give \(D\) with weight one. Starting in \(D\), those three groups of choices give \(T,S,D\) with weights one and multiplicities \(1,1,q-2\). These cases exhaust all possibilities and give the displayed matrix \(M_q(t)\). Multiplication by the all-ones column proves the exact population polynomial for all lengths by induction. Replacing \(t\) with \(u^{-1}\) and multiplying by \(u^{2n-3}\) gives the complete sphere-size distribution.

**3. Sharp maximum and its entire population.** The local defect terms are nonnegative, so the sphere size is at most \(2n-3\). For \(q\ge3\), repeating three distinct symbols cyclically produces a word with neither defect, proving attainability. Because the defect is a sum of nonnegative integers, equality holds if and only if both forbidden-factor counts vanish. Set \(t=0\) in the exact transfer formula to enumerate precisely these equality cases. Elementary inversion of the finite matrix \(I-zM_q(0)\) yields the displayed rational length enumerator. Equivalently its coefficients begin
\[
F_q(3)=q(q-1)(q+1),\quad F_q(4)=q(q-1)(q^2+q-5),\quad F_q(5)=q(q-2)(q-1)^2(q+4),
\]
and satisfy, for every \(n\ge6\),
\[
F_q(n)=(q-2)F_q(n-1)+(q-2)F_q(n-2)+(q-1)(q-2)F_q(n-3).
\]
These initial conditions and recurrence also provide an independent way to evaluate the rational expression.

**4. Mean.** A prescribed length-three factor is constant with probability \(q^{-2}\) under a uniform word. A prescribed length-four factor satisfies the collision criterion in exactly \(4q(q-1)\) of the \(q^4\) possible assignments, so its probability is \(4(q-1)q^{-3}\). Linearity of expectation in the deterministic sphere identity proves the stated mean; no independence between overlapping factors is assumed.

## Verification
The bundled self-contained Python program `verify_cyclic3.py` independently forms the actual output sets by all three local cyclic permutations. For each input it also computes the defect directly from local factors and checks the exact equality. Independently, it constructs the three-state population recurrence and checks every coefficient of the resulting distribution. The exhaustive regimes are \(q=2,3\le n\le11\), \(q=3,3\le n\le9\), \(q=4,3\le n\le8\), and \(q=5,3\le n\le7\), totalling 218584 source words over 27 parameter combinations. Each mean, maximum-size count, and claimed recurrence is checked when applicable. The accompanying `verify_cyclic3.log` records the counts and ends with `VERIFY_OK`. The infinite-length theorem follows from the preceding proof, not extrapolation from these finite checks.

## Relationship to prior work
Chen and Milenkovic, *Correcting Burst Errors with Applications to DNA-Based Data Storage*, arXiv:2610.15701v1 (first publicly submitted October 11, 2026), define cyclic substring permutation errors in their Section III and study binary three-symbol correction in Section V. Their results concern code redundancy, decoding and binary error patterns; they do not state the present nonbinary complete output-sphere population law, factor-collision identity or rational extremizer census. The binary subgroup/full-permutation equivalence is explicitly acknowledged and is not claimed as new.

For any nonbinary alphabet, the cyclic three-cycle subgroup is a proper restriction of all permutations of a length-three factor. The complete sphere-size law previously given for unrestricted length-three substring permutations consequently concerns a different output set: for an all-distinct input triple, the full symmetric group gives six possible outputs but the cyclic subgroup gives three. A generic regular-language transfer method does not provide the channel-specific defect identity or its evaluated three-state matrix without the collision classification.

## Limitations
This result treats a single exactly-length-three cyclic burst, not arbitrarily many bursts, unrestricted substring permutations, or the union of burst lengths up to three. It does not establish optimal code sizes, improved redundancy or practical decoding performance. The combinatorial spectrum is exact, but an equivalent unindexed treatment of these particular nonbinary local rotations remains a literature risk. No independent audit has been performed.

## References
1. Yuan-Pon Chen and Olgica Milenkovic, *Correcting Burst Errors with Applications to DNA-Based Data Storage*, arXiv:2610.15701v1, publicly submitted 2026-10-11, https://arxiv.org/html/2610.15701v1 (especially Sections III–V).
2. Related scientific record: *Two-state sphere spectrum for three-symbol permutation bursts*, identifier 3371874f-7756-4cd8-898e-7f326673fdfb (unrestricted permutation model; distinct from the cyclic subgroup studied here).
