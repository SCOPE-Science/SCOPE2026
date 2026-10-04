# Review

## Correctness
PASS. Expanding \(P^r\) and applying Parseval reduces the moment to pairs of multiplicity vectors with equal weighted frequency. For normalized gaps \(0<A<B\) with \(\gcd(A,B)=1\), every collision difference is exactly an integer multiple of \((-(B-A),B,-A)\). Its positive and negative masses are both \(|t|B\), which gives the exact resonance cutoff and the residual-triple coefficient formula. The first-resonance coefficient reduces to \(\binom{B}{A}\). The finite verifier checks these identities by exact integer enumeration over a broad independent range, but the proof itself is uniform and does not rely on that range.

## Originality
PASS, narrowly stated. Neuwirth's arbitrary-trinomial result is an \(L^\infty\) phase-extremal theorem, not an even-moment formula. Krenedits treats special signed idempotent trinomials primarily at non-even exponents. Pan--You--Wang--Zhou--Zhang--Chen explicitly give the no-collision/first-collision argument for the special support \(\{0,1,N\}\); that special case is treated as prior work here. Targeted published-results searches and primary-text inspection did not find the arbitrary coprime-gap formula, the explicit coefficient polynomial for every even moment, or the inverse recovery of \(A\) and \(B\) from the first phase response. The residual risk is that an older trinomial or moment-literature source states the same rank-one collision formula under different notation.

## Value
PASS. The moment at which phase first becomes observable is a natural spectral invariant, not an arbitrary numerical slice. The theorem identifies it exactly with the reduced diameter \(B\), gives the complete response at that first resonance, and shows that its width recovers the interior point \(A\) up to reflection. This turns the collision mechanism used in the three-term majorant literature into a complete arbitrary-spectrum phase-response classification and inverse statement.

## Closest literature and limitations
The closest inspected source is arXiv:2609.09740v2: it explicitly proves that the special family \(\{0,1,N\}\) has no power-collision for \(m<N\) and a first collision at \(m=N\). That implication is not claimed as new. arXiv:1006.0409v1 supplies the archive-era three-term majorant context, while arXiv:math/0703236v1 supplies the arbitrary-trinomial \(L^\infty\) comparison. The present claim is restricted to unimodular coefficients and even moments; higher-resonance optimization is left open.

Same-model review: passed. Independent audit: not yet performed.
