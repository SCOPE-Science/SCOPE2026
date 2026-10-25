# Independent mathematical audit

## correctness

PASS

Two irreducible individually reversible n-site nearest-neighbor row generators Q0,Q1 have stationary π0,π1 and invertible restrictions on V={row vectors v:v1=0}, dim n−1. Homogeneous symmetric switching at κ>0 forces each environment marginal 1/2. For r_e=2p_e and d=r0−r1, solving r0Q0=κd, r1Q1=−κd gives d(I_V−κ(R0+R1))=π0−π1, with R_e the inverse of Q_e on V. If the operator were singular for κ>0, one would construct a nonzero signed stationary vector of total zero mass for the irreducible 2n-state joint generator, contradicting uniqueness of its normalized stationary distribution. Hence D(κ)=det(I_V−κM)>0 for κ≥0 by D(0)=1. Detailed balance annihilates π_e f_e on each edge and the current is J=(κ/2)(π0−π1)(I−κM)^−1(R0 f0−R1 f1), with numerator adjugate degree≤dim V−1=n−2. A nonzero polynomial numerator has ≤n−2 positive zeros counted with multiplicity. For n=3, positive weights w0=(2,3,1),w1=(1,1,2) and conductances c0=(1,2,3),c1=(1,1,1) enforce detailed balance. Independently solving the 6×6 exact rational stationary generator yielded J(κ)=κ(5κ−2)/[2(469κ²+1236κ+792)] and unique positive zero at κ=2/5 with sign reversal, proving sharpness at n=3. Source VERIFY.py was materially inspected; its 187 logged checks alone do not establish all n. Edge-current normalization as unwrapped velocity/n and zero-current exceptional case were checked.

## originality

PASS

Best-of-knowledge PASS with bounded prior-coverage risk. Zhang 2010/2011 supplies general stationary motor velocities for two-state hopping, and the published 2003 minimal ratchet exhibits current nulls in a different switching scheme. These are prior current-computation frameworks and should not be claimed anew. The audited contributions are the all-cycle rate-polynomial zero bound under individually reversible uniform two-state switching and an explicit reversible 3-site rate-induced current reversal at κ=2/5. The prior general formula may admit specialization, but the inspected primary statements do not articulate the degree-sharp n−2 root obstruction or this exact witness; that requires additional zero-sum reduction and sign analysis.

## value

PASS

A rate-tuned reversal in a motor that is reversible within each landscape is a qualitative nonequilibrium transport phenomenon. The n−2 universal upper bound constrains the number of direction switches independent of rate magnitudes, while the exact smallest-ring saturator proves reversals occur despite microscopic detailed balance. Together they are useful structural facts for flashing-ratchet design and Markov transport rather than a routine finite matrix determinant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
