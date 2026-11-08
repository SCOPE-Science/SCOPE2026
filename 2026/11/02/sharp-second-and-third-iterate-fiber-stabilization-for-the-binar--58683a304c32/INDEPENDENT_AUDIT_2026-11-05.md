# Independent mathematical audit

## correctness

PASS

The four-letter morphism phi(0,1,2,3)=(01,02,31,32) has precisely the eight asserted adjacent bigrams, all present in phi^4(0), and their two substituted blocks exhaust all length-n binary factors for 2^h>=n. The binary tortoise T deletes the first 1 and appends 1. For any prefix p with at least k ones, T^k(pa)=D_k(p)a1^k; equality of T^k-images at n+1 therefore forces equal last letters and T^k(p)=T^k(q). Induction from a length-N class partition equality gives equality at all greater lengths. Fresh independent factor construction returned (n,k,factors,min_ones,T_classes,Tk_classes)=(13,2,96,3,88,87),(14,2,104,3,96,96),(17,3,128,4,120,119),(18,3,136,5,128,128). Counts coincide only in required base cases, and T^k factors through T, so same counts imply same partitions. Previous-length failures show b2=14,b3=18 sharp. The finite checks do not alone imply all-n; the prefix lemma does.

## originality

PASS

Campbell–Rampersad study tortoise factor-equivalence and iterates for paperfolding and Thue–Morse, whereas the claim classifies Rudin–Shapiro for k=2,3; one-pass complexity cannot imply equality of full k-pass fibers. No equivalent or stronger theorem was found in actual searches and inspected relevant arXiv text, but obscure automatic sequence identities remain possible.

## value

PASS

A sharp finite-to-infinite stabilization threshold for iterated equivalence relations in a canonical automatic sequence addresses a natural structural question; the reusable inheritance lemma and sharp predecessors give substance beyond tabulating factors. Only k=2,3 and this word are claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
