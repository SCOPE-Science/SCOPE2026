# Independent mathematical audit

## correctness

PASS

For n with sigma(n)|n², each factor sigma(p^e)|sigma(n) has prime support inside n. Prime powers p,p²,p³ are excluded because sigma(p^e)>1 and coprime to p. For pq with p<q, 1<p+1<=q and p+1 must be supported on q, hence p+1=q, forcing 2*3=6. For p²q, sigma(p²)=p²+p+1 is odd and coprime to p, so its prime support is confined to q, forcing q odd. Then sigma(q)=q+1 is even and its sole allowed non-q prime p must equal 2; sigma(4)=7 forces q=7 and n=28. For distinct p<q<r, p+1 supported on q or r and <=q forces p=2,q=3; then sigma(6r)=12(r+1)|36r² forces r+1|3, impossible. Both 6 and 28 pass direct divisor tests. A distinct independent exact SPF scan through n=160000 reproduced all such low-Omega solutions, and 364 yields the exact sharp nonperfect witness sigma=784, n²/sigma=169; infinity follows from the case proof, not the scan.

## originality

PASS

OEIS A090777 names precisely the sigma(n)|n² set and lists 6,28,120,364 etc with finite code. It does not state an unconditional classification by total prime-factor count Omega or the minimum Omega among nonperfect elements. A245787 imposes stronger tau(n)sigma(n)|n², which yields only a subset and is not a dominating theorem. The paper Amdeberhan–Moll–Sharma–Villamizar provides p-adic sigma valuation formulas/maximum bounds, not the exact low-Omega exclusion as a stated corollary; the current proof uses a dedicated prime-support and short factorization argument. Related strongly pseudoperfect Omega<=3 conclusions concern another property, with no shown implication to this set.

## value

PASS

An established divisor-sum divisibility set contains perfect and nonperfect members. The minimum prime multiplicity at which nonperfect members can arise is a canonical structural boundary; the n=364 witness and universal exhaustion of every smaller complexity shape make this an exact natural invariant, despite the brief elementary proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
