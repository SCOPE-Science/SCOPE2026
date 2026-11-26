# Independent mathematical audit

## correctness

PASS

Expanding (q−1)^j modulo q² gives the quotient digit weights w_j=(−1)^j(2m−1−2j), since paired exponents have opposite parity. In the group ring of Z/qZ, write e_x for the residue basis and J for its sum. Modulo the ideal of multiples of J, a nonzero internal weight contributes −e_{−w_j} (only digit q−1 is excluded), while a zero weight contributes q−1. A nonzero leading weight contributes −e_0−e_{−w_0} (digits 0 and q−1 are excluded); a zero leading weight contributes q−2. Since the internal weights sum to 1−m and all weights sum to m, multiplying gives the correction supported at m−1 and −m, or at m−1 alone for w_0=0. Restoring the unique constant term with total mass T gives the stated 2/q or 1/q subtractions. The two exceptional residues are distinct exactly when w_0 is nonzero. As q≥3 both levels occur and differ by the nonzero amplitude; the integer coefficients count actual digit choices, including m=1. The zero internal weights select one congruence class modulo q, so z≤ceil((m−1)/q) and division by T gives exponential decay of the discrepancy. Direct enumeration of actual integers matched every count for q=3,5,7,11,13,17, m=1–4, including both leading-weight branches. Replay: python3 /workspace/branches/619446a5-3748-4872-ad57-c3c7b5e4e801/independent_check.py.

## originality

PASS

Best-of-knowledge pass for the full all-odd-prime, exact fixed-length first quotient-lift spectrum. An indexed binary first-lift law exactly overlaps the q=3 specialization, so that case is not credited as distinct. The analogous first-layer result for all bases just counts palindromes in residue zero and cannot account for their distribution within that fibre modulo q². The examined coprime-modulus distribution theorems exclude this setting; use of familiar character methods is not claimed as new. Archival access limitations leave priority unresolved but do not supply positive coverage of the full claim.

## value

PASS

The first square-modulus lift of the forced divisor is the first place where these canonical even-length palindromes can have a nontrivial distribution. The theorem gives every count without enumerating the exponentially large catalogue, distinguishes the zero-leading-weight resonance, and proves nonuniformity at every length despite decay toward uniformity. This is a natural complete invariant, not just a numerical check for decimal divisibility or the already-covered binary specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
