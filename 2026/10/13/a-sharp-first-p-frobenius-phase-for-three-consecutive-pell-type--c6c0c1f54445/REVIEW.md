# Independent mathematical audit

## correctness

PASS

For u>=2, i>=2, A=P_i, B=P_{i+1}, C=A+uB, gcd(A,B)=1. Writing N=By+Aq with y in [0,A-1], the representations lift two-coin solutions (q-Bj,y+Aj) with 0<=z<=min(q-Bj,floor((y+Aj)/u)), giving exact count sum. For 0<=p<=K+1, K=floor(A/u), this proves first threshold q_p(y)=p if floor(y/u)>=p, otherwise B+p-floor(y/u)-1. Maximizing over residue classes proves g_p=B(A+up-1)-A for p<=K and the parity-dependent first break g_{K+1}=B(2A-1) if i even and B(2A-1)-A if i odd. Independent exhaustive coin-change dynamic programming checked residue crossing and maxima on bounded (u,i) grid; no inference beyond proved range.

## originality

PASS

Known p=0 follows immediately from the Sylvester two-coin result and is not credited. The primary Komatsu–Mu Pell-triple theorem treats (P_i,P_{i+2},P_{i+k}), so the base generators are different; generalized Fibonacci/Jacobsthal triplets also have different generator conditions. The full first-crossing residue formula and sharp breakpoint for consecutive triples are not implied by those statements. Risk: a generic theorem for redundant third denomination A+uB could dominate the claim.

## value

PASS

The representation count changes even when the third denomination is redundant for p=0. The first complete p-Apery phase, unique maximizing residues and parity-dependent exact first break supply useful sharp invariants of a naturally recurring coin family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
