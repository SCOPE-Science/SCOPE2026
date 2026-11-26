# Independent mathematical audit

## correctness

PASS

In the pair predecessor graph the states 00 and 10 have identical labeled outgoing behavior after merging; neither the recovered central bit nor the previous-bit determination for states B and C is lost. Each indexed closed walk recovers precisely one input, also with repeated neighbor sites at n=1,2. The zero factor is a diagonal projection T0<=I, so multiplying nonnegative factors preserves the entrywise bound under every deletion of T0. The remaining trace counts P_m by T1^3=T1+I and the three trace seeds. For n>=7 the Perrin numbers strictly exceed every lower-index term (check the prefix and use P_k-P_(k-1)=P_(k-5)); the only envelope tie when n=5 or 6 is n=6,m=5. Its one-zero fiber has size 3 since (T1^5)_(B,B)=2. T0 powers give the all-zero count 2 and P_1=0 forces the weight-one counts. Independent replay: `cd /workspace && python3 review_replay.py 2` checked every indexed input and fiber for n=1..16 using a bit-parallel Boolean rewrite of the truth table. The finite replay corroborates, not proves, the all-length claims; the frozen checker was inspected, not executed.

## originality

PASS

The specific distinct contribution supported here is the length-independent Hamming-weight envelope for all target words. Credit Powley's exact all-zero count, the prior homogeneous and periodic counting methods, and the precise overlap of the strict global maximum with the separately indexed 53a22033084e. Do not count those overlaps as additional novelty. The distinct mirror is dated later on its path (Nov 8 versus the frozen Nov 2 path); that dating alone is not a historical priority determination. Even disregarding chronology its actual bound has a different index and does not supply the weight envelope.

## value

PASS

The useful additional result is a bound on the probability of each output under uniform input that depends only on how many of its sites are one, even when the ambient ring is much larger. It constrains attainable one-step outputs and yields the natural worst-case inverse multiplicity without enumerating output patterns. The small exact quotient and projection give a structural reason for this sparsity effect, beyond recomputing the homogeneous recurrence or the global maximum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
