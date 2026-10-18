# Independent mathematical audit

## correctness

PASS

On any finite chain every isotone extensive idempotent map is ceil onto its top-containing fixed set, and it preserves meets. If every interval between consecutive common fixed points contains at most one private type, both compositions send each x to next common fixed point; if there is a mixed interval, choose earliest private u of type S-only then first later T-only v, obtaining j_S j_T(u)>j_T j_S(u). If they commute, their common image is in both fixed sets and bounded by least common fixed point, so composite equals ceil_B. Each block before a common fixed point has m noncommon positions labeled absent/S-only or absent/T-only without both kinds, exactly 2^(m+1)-1 words. Block OGF z/((1-z)(1-2z)); k-block coefficient yields R_{n,k}=[z^{n-k}](1-z)^(-k)(1-2z)^(-k). Sum gives OGF z/(1-4z+2z²) and c_n recurrence. Product nuclei decouple by meet decomposition into axis vectors (off-axis top forced by extensivity). Independent pairwise brute enumeration n<=7 reproduced c_n=1,4,14,48,164,560,1912 and joint ranks for each n; proof symbolic for all n.

## originality

PASS

The numerical integer sequence and general facts about nuclei/commuting closure operators are prior. Erné (2022), Lemma 3.6 and Cīrulis (2020), Proposition 3.5 cover the general implication that commuting nuclei/modal operators have a nuclear composite, but do not supply the chain-specific mixed-gap obstruction or k-refined ordered-pair census. OEIS A007070 contains c_n elsewhere; mere coincidence of counts is not claimed as new. The structural characterization and rank profile have best-of-knowledge novelty.

## value

PASS

Deciding exact commutation of modal nuclei from two fixed-point subsets on a chain is a natural finite Heyting-algebra question. The exclusive private-gap criterion gives a complete classification, and R_{n,k} refines the number of commuting pairs by composite-image size, a natural nontrivial statistic. The product rule extends this to all direct products; not just a recurrence copied from OEIS.

The dated certificate retains the supplied scientific assessment, sources and limitations.
