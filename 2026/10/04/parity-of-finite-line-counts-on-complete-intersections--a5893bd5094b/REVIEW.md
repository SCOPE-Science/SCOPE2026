# Review: Parity of finite line counts on complete intersections

## Correctness
PASS. Debarre--Manivel's coefficient formula reduces the line count to the coefficient of \(x^{n-1}\) in \((1-x)\prod_i q_{d_i}(x)\), with \(q_d(x)=\prod_{j=0}^d((d-j)+jx)\). If one degree is even, its endpoint factors contribute an even scalar factor. If every degree is odd, each block reduces modulo two to \(x^{(d+1)/2}\); the zero-dimensional hypothesis makes the total exponent exactly \(n-1\), giving coefficient one. The real consequence follows from conjugation pairing. The bundled checker independently replays the coefficient arithmetic on 209 admissible small cases and reproduces five standard benchmark counts.

## Originality
PASS with residual literature risk. The 1998 Debarre--Manivel paper supplies the general degree formula but does not state this parity classification. Their 2000 real-complete-intersection proposition is closely related: it uses mod-two characteristic-class methods for odd multidegrees, but its strict dimension hypothesis misses the zero-dimensional line boundary because in the present notation it becomes \(n-1>\sum_i(d_i+1)/2\), whereas zero expected dimension gives equality. Grünberg--Moree prove oddness for the hypersurface subfamily, not the arbitrary-multidegree converse. Broad published-finding corpus and literature searches for parity, congruences, Fano schemes, and real lines did not locate a statement implying the complete iff classification. A residual risk remains that the criterion is recorded implicitly in later Schubert-calculus or arithmetic Euler-class literature.

## Value
PASS. The result identifies a sharp, natural parity boundary for a standard enumerative invariant and immediately converts it into a real-existence theorem at precisely the zero-dimensional boundary omitted by the classical strict-dimension real-line criterion. It also unifies the parity pattern visible in the five classical complete-intersection Calabi--Yau threefold line counts and extends the known hypersurface oddness phenomenon.

## Closest literature and limitations
The closest source is Debarre--Manivel's 2000 real-complete-intersection paper, but its strict inequality excludes this boundary case. The claim is limited to general complete intersections with zero-dimensional Fano scheme of lines; no higher-plane parity theorem is asserted.

Same-model review: passed. Independent audit: not yet performed.
