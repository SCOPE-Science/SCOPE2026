# Independent mathematical audit

## correctness

PASS

The even half-coordinate is the permutation g=T3 modulo 2^r: g is the identity mod 2 and its derivative is odd. Odd inputs map into this permuted class in precisely one step. For G a power-of-two iterate, G′≡1 mod 4, so Taylor expansion of G(G(t))−t has valuation one more than G(t)−t whenever that difference is nonzero with valuation at least 3. The exhibited fixing time is a power of two, and the preceding power fails unless the point is already fixed; the period follows by divisibility. Splitting t by parity yields the stated cycle census, including r=0 and the fixed counts. For odd input 2u+1, the half-entry h is odd and its difference from the appropriate sign has valuation 1+2ν₂(u(u+1)); the other difference has valuation 1. This yields the periods and aggregate counts. For the incidence, the scaled cubic B(v)=v²(2^(s+1)v±3) is constant modulo 8 on odd v, and B′(v) has valuation exactly 1. For shifts 2^a with a≥2 all Taylor terms beyond the derivative have valuation at least a+2. The four roots at precision 3 begin the lifting induction: pairing roots separated by 2^(q−1) splits their outputs evenly at the next precision, and lifting each root duplicates it. The two signed entry classes each contain 2^j targets; g preserves their scaled unit modulo 8 and each target has period 2^j, so each class is one cycle. Restoring the discarded input bits gives 4·2^(s+1) odd predecessors per target. Independent finite corroboration: tabulated successors and odd indegrees, traversed the even cycles, and compared cycle counts, aggregate odd counts, occupied cycle counts and per-cycle-vertex indegrees for k=1 through 15 (65,534 residues). This corroborates, not proves, the general result; the uploaded verifier was inspected, not executed.

## originality

PASS

The even-state classification is known via T3, as the result acknowledges. The nonpermutation odd-tail placement is a supported distinct contribution relative to the inspected pre-existing work. Two later indexed same-map records directly cover the one-step odd indegrees (not merely a similar-looking polynomial), and in combination with even period information give the cycle-incidence refinement; they document later coverage and are not evidence of earlier priority.

## value

PASS

The natural nonpermuting monic cubic has depth-one tails for elementary reasons, but their placement is not read off from even periods. Identifying exactly two of ten occupied cycles per applicable period and computing uniform leaf multiplicities distinguishes their full nonfixed local graph structure, rather than just giving total period counts. The fixed-point leaf incidence is not claimed individually.

The dated certificate retains the supplied scientific assessment, sources and limitations.
