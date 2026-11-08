# Independent mathematical audit

## correctness

PASS

For the Thue–Morse fixed point mu(0)=01,mu(1)=10, any length-18 factor occurs in some mu^5(ab), a,b in {0,1}, because consecutive substitution blocks cover all four adjacent pairs; complete base enumeration yields 52 factors and exactly four 2-element fibres under twice removing first 1 and appending 1. Every nontrivial longer fibre projects to one of these four prefix pairs, so fibres remain disjoint pairs of forms {01z,10z} or {0110y,1001y}. A length>=5 left-special factor has a doubled letter (forbidden 01010,10101) fixing substitution parity; left specialness forces aligned even starts and lifts both preceding contexts. Desubstituting a left-special y of length>=14 and re-substituting yields both 0110y,1001y; the converse follows from common suffix contexts. Thus extra second-pass fibres biject with left-special factors of length n-4, yielding D2(n)=D1(n)+D1(n-2) for every n>=18. The n=17 counterexample D2(17)=5 versus 4 shows threshold sharp. Independent full-prefix factor enumeration verified n=17 and 103 lengths 18..120; infinite statement follows from parity/desubstitution, not checks.

## originality

PASS

Campbell–Rampersad 2026 establishes one-pass tortoise complexity on Thue–Morse and asks about higher iterates; one-pass D1(n) and special-factor counts are prior. The claimed D2(n)=D1(n)+D1(n-2) and four-pair structure are not among the full examined theorems. Prior second-iterate fibre upper bound two does not determine the number of nontrivial fibres. Best-of-knowledge PASS, with residual risk of alternate higher-iterate language.

## value

PASS

An exact second-iterate complexity classification for a canonical automatic word, with four primitive collision types and the sharp stability threshold 18, answers a natural higher-iterate question raised by the known one-iterate theorem. It is a complete infinite-family structural fact, not merely a numerical extension of a factor table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
