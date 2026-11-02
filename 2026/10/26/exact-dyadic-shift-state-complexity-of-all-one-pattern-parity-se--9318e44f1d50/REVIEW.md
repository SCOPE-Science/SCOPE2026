# Independent mathematical audit

## correctness

PASS

Carry recursion q'=floor((q+b)/2), digit d=(q+b) mod 2, trailing-one cap a and occurrence parity p tracks all output. Residual F_{q,a,p}(z)=p+s_m(z+q)+χ_m(a,ν2(z+q+1)) distinguishes equal q by parity and suitably chosen trailing-one counts. For distinct q, continuation z=2^K-q' yields oscillatory output from q versus constant from q', preventing merges. Reachable positive carry levels and zero-carry 2m states yield N_m(r)=2m+Σ_{k=0}^r A_m(k)+1_{r=m}. An independent full partition-refinement minimization checked 60 (m,r) pairs and exact direct outputs; all-size conclusion rests on residual proof.

## originality

PASS

Hendel’s full primary article concerns the underlying pattern-parity family and the 2m-state unshifted machine. Zantema–Bosma and Moradi–Rampersad–Shallit discuss general shift/subsequence automaticity and state bounds. None of the inspected direct claims provides this exact least-significant-first additive dyadic-shift formula, its lone correction or arbitrary-carry no-merging criterion. An equivalent k-kernel statement remains a priority risk.

## value

PASS

State complexity is a canonical computational invariant for automatic sequences. The new exact family-wide growth law (and isolated carry correction) goes beyond mere automaticity, with a structural proof of why no carry/trailing-pattern states merge; natural independent use in automata implementations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
