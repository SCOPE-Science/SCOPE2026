# Independent mathematical audit

## correctness

PASS

For each labeled n>=3 prism Y_n=C_n square K_2, local symbol a_i=(r_i,p_i,q_i) ranges over 000,010,001,011,100. For every cyclic three-column window the inequalities for covered counts on both vertices and non-addability of rung/top/bottom rail edges are necessary and sufficient for an inclusion-maximal matching. This yields 25 ordered-pair transfer states and 53 valid weighted arcs. The exact integer-polynomial Newton trace determinant is D(t,z)=(1+tz-t^3 z^2)(1-2tz-t^3z^2+t^3z^3-t^4z^3-t^5z^4), with degree 8, not a finite-z interpolation. The trace-log identity gives all n>=3 coefficients after subtracting spurious t and t^2 terms. Under t=s/y^2,z=y^3 the determinant has constant y-part (1-s^3)^2, hence no weight below ceil(2n/3); first y^0,y^1,y^2 coefficients yield exact least-size counts 6, 2n and n(5n-1)/3 for n modulo3. Independently direct enumeration of ALL edge-subset matchings for n=3,4,5,6 gave polynomials 6z^2+4z^3, 8z^3+9z^4, 40z^4+11z^5, 6z^4+72z^5+20z^6. The full infinite result follows from formal transfer algebra, not the finite counts.

## originality

PASS

Open-ladder maximal-matching polynomials in Došlić–Zubac and Hertz et al. are not the cyclic graph Y_n. OEIS A284703 already determines M_n(1) for prisms, and its denominator matches D(t,1); the ungraded count is explicitly excluded from novelty. The current statement retains z and determines each cardinality coefficient including minimum-size multiplicity by n mod 3, none of which follows from a single specialization z=1. No synonymous saturated-dimer enumerator covering the full bivariate polynomial was identified.

## value

PASS

The full labeled size distribution of inclusion-maximal matchings on a standard 3-regular periodic graph is a natural exact combinatorial invariant, and its sharp edge-domination/saturation minimum and number of optimal saturated configurations provide structurally useful quantitative detail beyond already tabulated totals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
