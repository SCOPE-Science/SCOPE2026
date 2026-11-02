# Independent mathematical audit

## correctness

PASS

Valid positive binary strings have language 1(1|00)*. Length-m suffix-value lists V_m split in increasing numerical order as V_(m−2) concatenated with 2^(m−1)+V_(m−1), and hence internal gaps W_m split into W_(m−2), one bridge G_m, W_(m−1). A fixed G_m bridge occurs F_(L−m) times inside positive support elements of binary length L, and all length-boundary gaps alternate between 1 and 2. Summation L=m+1..K gives F_(K−m+2)−1; prefix support count F_(K+2) and gap count F_(K+2)−1. G2=G3=3 and others distinct; Fibonacci ratios give limiting point masses and exact geometric tail. Since G_m grows like 2^m and φ<2 the mean diverges. Direct independent binary predicate against complete histogram for K=1..16 passed. These prefix checks do not prove unbounded K or the tail law.

## originality

PASS

The Baum–Sweet support itself and Fibonacci recurrence are known, including the equivalent closure language in OEIS A060142 and automatic sequence A086747. Those sources characterize support sites, not the exact all-K adjacent-return gap counts by each bridge scale or the size-biased heavy-tailed limiting distribution. Unlike a new binary indicator definition, the claimed contribution is a complete statistical invariant extracted from the known language.

## value

PASS

The complete return gap spectrum and exact dyadic-prefix probability law describe a natural and mathematically useful recurrence invariant of a classical automatic sequence. Heavy tail and infinite mean despite structured Fibonacci support growth is a notable sharp classification, with clear sampling convention and exact finite histogram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
