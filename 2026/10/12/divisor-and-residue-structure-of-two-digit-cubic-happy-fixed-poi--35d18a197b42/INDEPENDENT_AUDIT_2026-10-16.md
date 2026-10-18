# Independent mathematical audit

## correctness

PASS

The fixed-point equation a³+c³=ab+c rearranges exactly to a(b−a²)=c(c−1)(c+1). For c≥2, a is any positive divisor of c³−c and b=a²+(c³−c)/a uniquely; b>a,c follows by considering a>c and a≤c, so count τ(c³−c) is exact, not just formal factorization. For a=2^e m, odd p-power factors of c(c−1)(c+1) give residues −1,0,1; powers of 2 yield 1,2,3,5 residue classes for e=0,1,2,≥3. CRT gives r(e)3^{ω(m)} /a density. Cases c=0,1 require b=a² and a≥2. Independent exhaustive divisor/digit tests for 2≤c≤250 and residue counts for 2≤a≤500 agree; these are corroboration to unrestricted proof.

## originality

PASS

Finite-base cubic fixed-point tables in Wu–Dang–Zhang and OEIS A193594 do not provide the varying-base complete divisor parametric family or fixed-leading-digit prime-power residue density. Hargreaves–Siksek exact fixed points address exponent 2, not 3 in the accessible abstract; its full text could not be accessed and Oxford attempt returned worker unavailable, retained as residual risk. Best-of-knowledge originality for the exact two-digit CRT classification, not for the trivial rearrangement.

## value

PASS

Two-digit fixed points of the sum-of-cubes-of-digits dynamical map are a standard natural subproblem. Beyond a bare algebraic substitution, the theorem gives the complete varying-base parametrization, exact divisor-count layer τ(c³−c), and nontrivial local-to-global leading-digit residue distribution with exceptional 2-adic factor. Researchers studying base-dependent digit dynamics could use this full classification as a precise boundary and source of infinite families; no claim about all digits/cycles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
