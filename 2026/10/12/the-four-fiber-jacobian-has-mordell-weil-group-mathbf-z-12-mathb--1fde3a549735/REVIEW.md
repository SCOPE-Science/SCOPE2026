# Independent mathematical audit

## correctness

PASS

Sun–Xu’s explicitly resolved F_3 pencil in characteristic 5 has 12 blowups and Picard rank 14. The fiber F=2C_0+6Γ−Σe, the t=0 strict transforms A,B and ten E_{a,i}=e_{a,i}−e_{a,i+1} (1≤i≤5), and the t=∞ component C_0 generate the 13-dimensional vertical subgroup. Independent SymPy determinantal computation on its complete 14×13 integer matrix yields rank13, maximal minors [0,24,−12,12,−12,12,−12,12,−12,12,−12,12,−12,12], gcd12. Inspected bundled verify.py identifies a 12×12 determinant ±1, hence SNF 1^12,12. Restriction from regular S to smooth generic C has vertical kernel, Pic(C)=Z⊕Z/12; horizontal final exceptional meets F once, supplying rational section and degree split, so J(k(t))=Z/12. This is an integral full-lattice computation, not rank-only inference; valid only for specified characteristic-5 fibration.

## originality

PASS

Sun–Xu’s section 5 supplies full fiber geometry but not this precise MW torsion group. Earlier Saito/Nguyen constructions of related pencils and general Shioda/Gong–Xu rank methods do not state the characteristic-5 integral SNF nor force order12 from rank zero. Resultary returned no corresponding exact torsion statement. Literature priority risk persists for the older pencil papers, some full text unavailable.

## value

PASS

The full Mordell–Weil group is a central arithmetic invariant of the newly explicit four-singular-fiber genus-two surface. Determining its exact torsion order 12 via an unsaturated vertical lattice is information not supplied by general rank formulas and naturally useful in comparing reductions and fibration arithmetic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
