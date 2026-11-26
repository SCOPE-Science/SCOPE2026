# Independent mathematical audit

## correctness

PASS

At height r, both coordinates have modulus at most r, including in the strictly negative sector because both moduli are at least one. In 0<lambda<1/r the floor is -1 on negative first coordinates and 0 otherwise. The four sector phases in the proof are disjoint classes modulo 4r+1 (the nonnegative sector also contains zero). Substituting the sector transitions adds one, including the branch from (r,0) to (0,r); this yields all 4r+1 distinct states and the summed point count. Above or at 1/r the image of (r,0) has strictly larger height. For q>=2 at lambda=1/q, floor(-q/q)=-1; among first coordinates in [-q,q], only x=q has changed from the protected rule. On C_{q+1} the sole |x|=q+1 points have phases 0, 2, 4q+3; the x=q points have phases 4, 4q+1. Thus the initial jump to phase 5 runs without intervening exceptions until phase 4q+1 at (q,1), where the next jump returns to phase 1 of C_q. The 4q subsequent steps return to phase 0 for the first time. Counting both jumps and the outer arc gives 8q-2, including 4q-3 outer points and every inner-shell-q point, with no repetition before return. Lower shells stay protected. Inspected but did not execute the frozen checker. Own direct integer iteration (/tmp/opencode/frozen-review-replay.py, section 1) reproduced the least periods and shell counts for q=2,3,4,17,101 at resonance and at 2/(2q+1); the phase proof supplies the universal quantifiers.

## originality

PASS

The supported contribution is the exact all-q first-resonance period and two-shell itinerary for the named axis seed, proved together with its protected-shell baseline. The map and near-integrable setup are prior, and protected pointwise floor agreement alone is routine. The closest prior statements checked give qualitative periodicity, density, or parameter methods, not this uniform least period and shell composition.

## value

PASS

The first floor change is forced by the maximal coordinate of a natural central shell. At that forced threshold, the exact itinerary explains how two levels are joined and gives a uniform least-period jump, rather than merely a proof of recurrence at selected parameters. This controls the first activation in a well-studied difficult lattice-dynamics family without implying global periodicity or a law for later crossings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
