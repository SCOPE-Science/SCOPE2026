# Independent mathematical audit

## correctness

PASS

PASS. For n>=1 and r>=2 weak ordered compositions, the Φ_d exponent of each Gaussian multinomial is floor(n/d)-sum_i floor(k_i/d), the nonnegative residue carry. Maximizing ∑(k_i mod d) subject to r residues each <d and sum n gives E_d=min(floor(n/d),floor((r(d-1)-n mod d)/d)); attainability follows by filling bounded digits and adding remaining multiples of d. This yields polynomial lcm factorization for all d=2..n. For a fixed p, carry vectors obey 0<=n_j+p c_{j+1}-c_j<=r(p-1) with zero endpoints; reconstructing digits proves realizability and a crossing-coordinate comparison proves closure under componentwise maximum. Therefore one tuple attains all p^j maxima simultaneously and Legendre's formula yields the integer lcm p-adic exponent ∑E_{p^j}; cyclotomic Φ_{p^j}(1)=p proves exact q=1 specialization. An independently written integer enumeration checked all compositions for n<=11 and 2<=r<=5 against E_d and simultaneous p-carry maxima; finite checks do not prove the all-n result.

## originality

PASS

PASS, with explicit acknowledgment of more relevant prior primary Chen–Hou. The cyclotomic factorization of *individual* q-multinomials is already Chen–Hou Lemma 1, with Guo's LCM theorem for r=2. The claim surviving is the sharp simultaneous r-part row LCM exponents and the nontrivial q→1 specialization through coordinatewise maximal carry vectors. Howard's ordinary multinomial valuation-frequency theorem supplies a potential general counting framework, not the stated polynomial LCM/specialization. This is a qualified new parameterized invariant despite use of classical factors.

## value

PASS

PASS. Polynomial LCM for a natural Gaussian multinomial row across arbitrary r is an exact all-parameter invariant with prime-power exponents possibly exceeding one, unlike r=2. Specialization to the integer multinomial LCM is NOT automatic for arbitrary integer polynomials; the carry-lattice closure exhibits a structural compatibility with arithmetic interest beyond a routine restatement of a Gaussian factorization lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
