# Independent mathematical audit

## correctness

PASS

Averaging the two initial-sign characteristic functions gives f''+2λf'+v²f=0 with f(0)=1, f'(0)=0. Depolarization commutes with the rotations. In the computational-basis Choi matrix the coherence is the |00><11| entry e^(-κt)f/2, and partial transpose places it in the block with both diagonal entries (1-e^(-κt))/4. Its smaller eigenvalue is the PPT minimum, so equality is entanglement breaking. The initial positive lobe decreases to zero. On each later lobe log(|f|/h_κ) has second derivative -ω²csc²(ω(t-z_j))+[κ/(2sinh(κt/2))]²<0 since t>π/(2ω); the positive set is one interval or empty. The rate quotient vanishes at lobe endpoints, is positive inside, and strictly decreases under translation by π/ω, even without telegraph damping. Its value at the |f| peak and the upper estimate replacing the denominator by the left zero establish the bounds. For fixed λ>0 these squeeze the counting index to within O(1) of the solution of 2e^(-λt)/t=κ (bounded shift of lobe index absorbs the multiplicative error), giving W(2λ/κ). For λ=0 the squeeze is between inverse-time denominators a fixed distance apart and gives the inverse-rate law. At and above critical damping f is positive and strictly decreases for t>0, so only the initial crossing occurs. Independent replay: python3 /workspace/branches/independent_checks.py 1; 30 propagator/PPT pairs and nine revival count inversions.

## originality

PASS

The input channel construction, telegraph coherence, qubit entanglement-breaking criterion and qualitative strong-coupling revivals have precedents. The supported distinct contribution is the exact strictly ordered lobe thresholds (including equality and interval topology) and sharp count with bounded remainder for the specified independently depolarized channel.

## value

PASS

For a standard exactly soluble noise model combined with a separately calibrated depolarizer, the hierarchy identifies which individual revivals survive. The explicit logarithmic count with a negative log-log correction, and its change to inverse-rate behavior for static noise, quantify a qualitative revival picture with an operationally meaningful channel observable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
