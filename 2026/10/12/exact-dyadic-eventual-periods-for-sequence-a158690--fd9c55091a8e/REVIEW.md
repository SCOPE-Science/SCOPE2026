# Independent mathematical audit

## correctness

PASS

The formal identity H(e^t-1) gives integer c_m and a(n)=sum_{m<=n} c_m m! S(n,m). With h=2^{k-1}, odd j satisfy (j^h-1)/2^{k+1}=(j^2-1)/8 mod4; even j^n terms vanish at the stated n>=k+3 bound. The weighted functions U_epsilon have Delta^8 U=0 mod4, leaving exact c_0..7=(1,1,2,7,33,197,1419,11966), whose weighted sums are 2 for even n and 0 for odd. This yields half-shift obstruction and a full shift 2^k for all n>=k+3. Since any minimal eventual period divides 2^k and 2^{k-1} fails, it equals 2^k. Independent integer Stirling recurrence checked the period and obstruction for r=5..8; finite checks do not prove all powers.

## originality

PASS

PASS (best of knowledge): Kallat establishes lambda(2^r)=2^(r-2) as an eventual period but does not resolve the least eventual period; OEIS records isolated small-modulus behavior. The present parity-sensitive half-period congruence simultaneously proves existence of 2^(r-3) and excludes all smaller powers for every r>=5, a genuinely stricter infinite parameter conclusion. The Stirling representation and general eventual periodicity themselves are attributed to prior work. No indexed exact full-family result found in reviewed records.

## value

PASS

PASS: Sharp exact eventual-period classification for every dyadic modulus resolves a natural infinite arithmetic invariant of a named sequence, refining a known universal period by a factor of two with an obstruction ensuring minimality. A single small-modulus sample would not suffice, but the proof covers all r>=5.

The dated certificate retains the supplied scientific assessment, sources and limitations.
