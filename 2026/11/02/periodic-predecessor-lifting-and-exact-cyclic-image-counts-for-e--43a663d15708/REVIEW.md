# Scientific review of corrected Rule 126 statement

## Correctness — PASS
For the exact cyclic local rule, the boundary variables d_i=x_i XOR x_{i+1} satisfy y_i=d_{i-1} OR d_i and must have even total parity. Conversely, every compatible even boundary word integrates to two periodic inputs. Zero-separated one-runs yield the stated parity obstruction, including the unrestricted choice at length >=4. The all-one target is exceptional: n=1 is impossible, but 1^k is reachable for every k>=2 (for odd k>=3 use a boundary word with exactly one zero). In particular x=001 maps to 111, so the older claim that all failed same-period targets exclude every odd multiplier was false. For nonconstant obstructed targets, forced odd parity repeats k times and the exact multiplier set is the even integers. The 4-state 010-avoiding trace and signed cyclic block enumerator give the exact all-length R_n formula. Independent checks rebuilt direct images through n=17 and exposed/repaired the singleton exception.

## Originality — PASS with documented risk
Martínez et al. (arXiv:1212.0124v1, Sections 2 and 3) discuss the already-known 010 forbidden factor, periodic basins and de Bruijn methods; OEIS A269173 already has the local bitwise identity. Those known ingredients are not claimed as new. The corrected all-length same-period parity classification for nonconstant targets, exceptional singleton, and exact indexed image count were not found in accessible primary results or published mathematical-record searches. McIntosh's 2009 monograph remains uninspected; equivalent historical results remain possible.

## Value — PASS
The corrected theorem distinguishes bi-infinite permissible outputs from exact-period liftability in a canonical cellular automaton, provides a sharp period-doubling obstruction with infinitely many witnesses, and determines a rational all-length image census. The singleton boundary exception is mathematically necessary for a correct universal periodic formulation.

## Scope and provenance
Only one synchronous step on indexed binary rings is claimed; not general multistep images, least-period predecessor classification or noise. The scientific correction alters RESULT.md and SLOGAN.txt as well as this review and AUDIT.json; it is a substantive repaired claim, not a pass of the erroneous original. Finite computations corroborate but do not prove the all-length statements. The untouched machine/formal/expert verification record is preserved.
