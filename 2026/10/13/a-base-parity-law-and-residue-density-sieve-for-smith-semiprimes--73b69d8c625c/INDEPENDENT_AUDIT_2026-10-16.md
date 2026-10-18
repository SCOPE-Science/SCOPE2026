# Independent mathematical audit

## correctness

PASS

The digit-sum congruence s_B(n)=n mod(B-1) gives (p-1)(q-1)=1 mod m for n=pq, including p=q. If B is odd, m even: all cases except p=q=2 contradict parity; base 3 gives s_3(4)=2!=4, while every odd B>=5 has s_B(4)=4=2s_B(2). For even B, m is odd: distinct prime residues satisfy r,T(r)=1+(r-1)^(-1), r in A_m with r,r-1 units, and T is involutive. CRT counts |A_m|=prod l^(a-1)(l-2). Standard fixed-modulus PNT in AP plus Mertens estimates and Brun-Titchmarsh bound each ordered residue prime-pair contribution to x loglog x/(phi(m)^2 log x); prime squares are lower-order. This is the density of the NECESSARY congruence-compatible superset C_B, not the true Smith subset M_B. Independent direct digit sums for all semiprimes <=30000 in B=2..20 confirm odd-base classification; checked T for odd moduli up to 39 and decimal A_9={2,5,8}, c_10=1/12. Finite enumeration does not establish the asymptotic.

## originality

PASS

Smith semiprime sequences and the decimal digital-root residue restriction are prior; OEIS A279314 already explicitly describes modulus B-1 in arbitrary bases. The assessed surviving statement is the exact odd-base semiprime classification plus all-even-base involutive residue pairing and its asymptotic semiprime-compatibility sieve, not claimed novelty of congruence (1) or decimal patterns.

## value

PASS

The all-odd-base complete semiprime classification and closed all-even-base asymptotic sieve constant quantify a natural base-dependent obstruction. The density theorem is a genuine arithmetic counting statement over infinitely many prime pairs, not a finite-table recomputation; modest complexity is compensated by complete explicit parameter coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
