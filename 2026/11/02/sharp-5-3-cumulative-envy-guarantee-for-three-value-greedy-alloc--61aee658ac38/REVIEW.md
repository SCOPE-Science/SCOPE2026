# Independent mathematical audit

## correctness

PASS

Scaling u to1 gives greedy gap g in {0,1,2,3}, competitor signed gap d in Z. The displayed nonnegative 24-entry potential P(g,|d|) supported on |d|<=5 satisfies 3|g-v|-5|d±v|+P(|g-v|,d±v)<=P(g,d) by exhaustive finite g=0..3, |d|<=8, v=1,2,3, signs± checks. For |d|>=9 both potential entries vanish, |d±v|>=6 and 3g’<=9<5*6; hence all integer states covered. Telescoping from P(0,0)=0 and final nonnegative potential proves G<=5O/3 for ANY comparison allocation, all m. The repeated (1,1,3,1)(2,3,1)^r yields greedy cost 6+5r, feasible competitor cost 4+3r, so asymptotic ratio at least5/3. Independent exhaustive transition checks d in [-30,30] and exact small-sequence DP and witness family agree; infinite proof rests on full transition analysis.

## originality

PASS

Cumulative envy model and fixed-order offline hardness are established by Goldberg–Robinson–Teh; their publicly accessible abstract presents a 3/2 guarantee for a variant permitting ordering control. It is not the same ternary fixed-order lower-load greedy result. Full primary manuscript inaccessible; best-knowledge originality with material residual risk.

## value

PASS

Sharp universal online-to-offline cumulative-envy price for the first three-valued alphabet beyond two-valued greedy exactness, with a concrete recurring obstruction and a global potential. Exact general-in-horizon guarantee rather than isolated tiny numeric gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
